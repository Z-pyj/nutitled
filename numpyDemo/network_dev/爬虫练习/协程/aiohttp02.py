# 并发限制，一般可以借用asyncio的semaphore来控制并非量
import asyncio
import aiohttp

# 设置最大并发
CONCURRENCY = 5
URL = 'https://www.baidu.com'
# 通过asyncio.Semaphore方法控制并发，然后放到对应的爬取方法中，使用 async with 将semaphore作为上下文对象即可
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    # async with 将semaphore作为上下文对象
    async with semaphore:
        print('scraping:', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    # 定义任务对象列表1000个
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(1000)]
    # asyncio.gather从给定的 coroutinesfutures 返回一个未来的聚合结果
    await asyncio.gather(*scrape_index_tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
