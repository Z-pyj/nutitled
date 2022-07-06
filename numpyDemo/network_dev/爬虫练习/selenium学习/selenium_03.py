import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import EdgeOptions

# TODO:无头模式，headless，无头模式下，在网站运行时不会弹出窗口，从而减少资源的加载

option = EdgeOptions()
option.add_argument('--headless')
browser = webdriver.Edge(options= option)
browser.set_window_size(1366, 768)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('./preview.png')

