import requests

r = requests.get('https://www.baidu.com')
# <class 'requests.models.Response'>
print(type(r))
# 响应码
print(r.status_code)
# 响应体类型
print(type(r.text))
# 响应体
print(r.text[:100])
# cookie
print(r.cookies)


