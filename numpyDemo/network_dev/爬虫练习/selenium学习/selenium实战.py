import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import EdgeOptions
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 1
browser = webdriver.Edge()
wait = WebDriverWait(browser, timeout=TIME_OUT)


# 基础方法爬取内容
def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        time.sleep(5)
        wait.until(condition, condition(locator))
    except TimeoutException:
        logging.error('error occurred scraping %s', url, exc_info=True)


# 爬取列表
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    # 拿到所有节点才算成功
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


# 解析内容，获取href用于拼接url
def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


# 爬取详情页
def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '.item h2'))


# 解析详情页
def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.CSS_SELECTOR, '.item h2').text
    categories = [ele.text for ele in browser.find_elements(By.CSS_SELECTOR, '.item .category span')]
    score = browser.find_element(By.CSS_SELECTOR, '.item .score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.item .drama p').text

    return {
        'url': url,
        'name': name,
        'categories': categories,
        'score': score,
        'drama': drama
    }


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info('detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)
    finally:
        browser.close()


if __name__ == '__main__':
    main()
