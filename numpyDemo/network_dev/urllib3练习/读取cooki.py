import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
# load()方法读取本地文件
cookie.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
# build_opener()方法构建Opener()
opener = urllib.request.build_opener(handler)
# 执行open函数
response = opener.open('http://www.baidu.com')

print(response.read().decode('utf-8'))
