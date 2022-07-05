import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import EdgeOptions
from selenium.webdriver import ChromeOptions
# TODO:反屏蔽,利用CDP,chrome开发工具协议实现在每一个页面加载的时候就执行JavaScript语句，将webdriver属性置空
# cdp方法叫做：Page.addScriptToEvaluateOnNewDocument
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)


browser = webdriver.Edge(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source':'Object.defineProperty(navigator, "webdriver", {get:() => undefined})'
})
try:
    browser.get('https://antispider1.scrape.center/')
    time.sleep(3)

finally:
    browser.close()