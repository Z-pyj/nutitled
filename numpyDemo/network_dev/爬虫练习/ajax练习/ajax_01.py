import pymongo
import requests
import logging
import time
LIMIT = 10
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']


# 通用接口
def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error ocurred while scraping %s', url, exc_info=True)


# 电影列表
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


# 电影详情
def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)


if __name__ == '__main__':
    TOTAL_PAGE = 10
    for page in range(1, TOTAL_PAGE + 1):
        time.sleep(3)
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            scrape_id = item.get('id')
            detail_data = scrape_detail(scrape_id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)
            logging.info('data saved successfully')
