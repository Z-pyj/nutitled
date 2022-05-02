import urllib.request, http.cookiejar

# 声明CookieJar()对象
cookie = http.cookiejar.CookieJar()
# 利用HTTPCookieProcessor()构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# build_opener()方法构建Opener()
opener = urllib.request.build_opener(handler)
# 执行open函数
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)
