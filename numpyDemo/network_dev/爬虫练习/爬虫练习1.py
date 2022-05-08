import requests
import json
import re
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists
import multiprocessing

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

BASE_URL = 'https://ssr1.scrape.center'

TOTAL_PAGE = 2
RESULT_DIR = 'result'
exists(RESULT_DIR) or makedirs(RESULT_DIR)


# 保存数据
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# 获取页面源码
def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error_occurred while scraping %s', url, exc_info=True)


# 实现翻页
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


# 解析列表页
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)" class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url


# 详情页源码
def scrape_detail(url):
    return scrape_page(url)


# 解析详情页
def parse_detail(html):
    cover_pattern = re.compile('class="el-card.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映', re.S)
    score_pattern = re.compile('class="score m-t-md m-b-n-sm">(.*?)</p>', re.S)
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()) if re.search(score_pattern, html) else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published': published,
        'drama': drama,
        'score': score
    }


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully!')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE+1)
    pool.map(main, pages)
    pool.close()
    pool.join()
