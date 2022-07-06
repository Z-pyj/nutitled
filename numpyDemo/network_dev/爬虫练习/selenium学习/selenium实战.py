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


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_url = parse_index()
            logging.info('detail url \n %s', list(detail_url))
    finally:
        browser.close()


if __name__ == '__main__':
    main()
