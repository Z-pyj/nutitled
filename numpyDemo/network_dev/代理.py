from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 代理
proxy_handler = ProxyHandler({
    'http': 'http://192.168.31.36:8080',
    'https': 'https://192.168.31.36:8080'
})
# build_opener方法构建一个Opener
opener = build_opener(proxy_handler)

try:
    # 发送链接
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
