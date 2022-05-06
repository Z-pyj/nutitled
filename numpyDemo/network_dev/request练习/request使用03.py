import requests

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# # 会话也可用来为请求方法提供缺省数据
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test1': 'true'})
#
# r = s.get('http://httpbin.org/headers', headers={'x-test2':'true'})
# print(r.text)
#
# hd = r.request.headers
# print(hd)

# # 没有ssl证书，报错抛出 SSLError
# requests.get('https://requestb.in')

# # 设置ssl
# requests.get('https://github.com', verify=True)
#
# # 为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径
# requests.get('https://github.com', verify='/path/to/certfile')
#
# # 将其保持在会话中
# s = requests.Session()
# s.verify = '/path/to/certfile'

# requests.get('https://kennethreitz.org', verify=False)

# # 响应体内容工作流
# with requests.get('http://httpbin.org/get', stream=True) as r:
#     print(r.content)

# 代理
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

r= requests.get(url='http://example.org', proxies=proxies)
print(r.content)