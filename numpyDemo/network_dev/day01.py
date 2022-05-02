import urllib.request
import urllib.parse
import urllib.error
import socket

if __name__ == '__main__':
    #     url = 'https://python.org'
    #     # urlopen()请求网址
    #     response = urllib.request.urlopen(url)
    #     # 获取响应内容
    #     print(response.read().decode('utf-8'))
    #     # 响应类型为<class 'http.client.HTTPResponse'>
    #     print(type(response))
    #     # status属性获取响应码
    #     print(response.status)
    #     # getheaders()方法获取所以请求头
    #     print(response.getheaders())
    #     # getheader()获取请求头中某属性的值
    #     print(response.getheader('Server'))
    #
    # # data参数
    #     data = bytes(urllib.parse.urlencode({'name': 'zw'}), encoding='utf-8')
    #     response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
    #     print(response.read().decode('utf-8'))
    # # timeout参数
    #
    #     try:
    #         response = urllib.request.urlopen('https://www.httpbin.org/get',timeout=0.1)
    #     except urllib.error.URLError as e:
    #         if isinstance(e.reason, socket.timeout):
    #             print('TIME OUT')
    # request类
    url = 'https://httpbin.org/post'
    dicts = {
        'name': 'zw'
    }
    data = bytes(urllib.parse.urlencode(dicts), encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36 '
    }
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
