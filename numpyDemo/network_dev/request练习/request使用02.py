import json

import requests
import uiautomator2 as u2

url1 = 'https://httpbin.org/get'
# r= requests.get(url1)
# print(r.text)

# # params拼接参数
# data = {
#     'name': 'zw',
#     'age': 23
# }
#
# r = requests.get(url1, params=data)
# # print(r.text)
# # print(r.json())
# print(r.encoding)
# print(r.content)
# print(r.raw)
#
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r1 = requests.post('http://httpbin.org/post', data=payload)
# print(r1.text)
#
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# data=json.dumps(payload)
# print(data)
# print(type(data))
# r = requests.post(url, data=json.dumps(payload))
# print(r.text)

# url = 'http://httpbin.org/post'
# files = {
#     'file': open('./request使用01.py', mode='rb')
# }
# r = requests.post(url, files)
# print(r.text)

# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# print(bad_r.raise_for_status())

# url = 'http://example.com/some/cookie/setting/url'
# url1 = 'http://www.baidu.com'
# r = requests.get(url=url1)
#
# print(r.cookies.values())

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# url1 = 'http://httpbin.org/elsewhere'
# r = requests.get(url1, cookies=jar)
# print(r.text)

# r = requests.get('http://github.com')
# print(r.status_code)
# print(r.history)
#
# r = requests.get('http://github.com',allow_redirects=False)
# print(r.status_code)
# print(r.history)

# 超时
r = requests.get('http://github.com',timeout=0.01)