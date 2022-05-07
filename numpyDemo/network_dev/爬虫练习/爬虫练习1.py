import requests
import json
import re
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

BASE_URL = 'https://ssr1.scrape.center'

TOTAL_PAGE = 10


# 获取页面源码
def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error_occurred while scraping %s', url, exc_info=True)


# 实现翻页
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    print(index_url)
    scrape_page(index_url)


if __name__ == '__main__':
    scrape_index(2)
