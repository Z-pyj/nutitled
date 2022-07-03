import json
import logging
import asyncio
import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 10
CONCURRENCY = 5
ids = []
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'book'
MONGO_COLLECTION_NAME = 'books'
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client['MONGO_DB_NAME']
collection = client['MONGO_COLLECTION_NAME']


# 通用爬取方法
async def scrape_api(url):
    # 设置并发量
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            # session的get方法请求url
            async with session.get(url) as response:
                # 返回一个协程对象
                return await response.json()
        except aiohttp.ClientError:
            # 如果出现错误，输出异常
            logging.error('error occurred while scraping %s', url, exc_info=True)


# 保存数据
async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)


# 爬取列表
async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


# 爬取详情
async def scrape_detail(id):
    url = DETAIL_URL.format(id)
    data = await scrape_api(url)
    await save_data(data)


async def main():
    global session
    session = aiohttp.ClientSession()
    # 爬取列表页的所以task组成的列表
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    # task作为asyncio.gather方法的参数，赋值给result，由所以task返回结果组成的列表
    results = await asyncio.gather(*scrape_index_tasks)
    # 获取id,作为详情地址id的参数
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    # 详情页task任务列表
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    # 调用asyncio.wait，并将task列表传入
    await asyncio.wait(scrape_detail_tasks)
    # 关闭session
    await session.close()
    logging.info('result %s', json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
