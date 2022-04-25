import urllib.request

if __name__ == '__main__':
    url = 'https://python.org'
    # urlopen()请求网址
    response = urllib.request.urlopen(url)
    # 响应类型为<class 'http.client.HTTPResponse'>
    print(type(response))
    # status属性获取响应码
    print(response.status)
    # getheaders()方法获取所以请求头
    print(response.getheaders())
    # getheader()获取请求头中某属性的值
    print(response.getheader('Server'))
