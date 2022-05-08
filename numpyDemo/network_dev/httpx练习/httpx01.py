import requests
import httpx

# url = 'https://spa16.scrape.center/'
# r = requests.get(url)
# print(r.text)

url1 = 'http://www.baidu.com'
response = httpx.get(url1)
# print(response.text)
h = response.headers
print(h)