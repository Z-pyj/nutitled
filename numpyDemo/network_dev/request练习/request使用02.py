import requests

url1 = 'https://httpbin.org/get'
# r= requests.get(url1)
# print(r.text)

# params拼接参数
data = {
    'name': 'zw',
    'age': 23
}

r = requests.get(url1, params=data)
# print(r.text)
print(r.json())
