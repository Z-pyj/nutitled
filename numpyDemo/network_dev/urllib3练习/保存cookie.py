import urllib.request, http.cookiejar

filename = 'cookie1.txt'
# MozillaCookieJar()是CookieJar的子类出来cookie和文件相关事件
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
