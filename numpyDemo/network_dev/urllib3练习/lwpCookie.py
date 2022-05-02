import http.cookiejar
import urllib.request

filename = 'cookie2.txt'
# CookieJar()同样可以保存和读取cookie，保存的格式LWP格式
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)