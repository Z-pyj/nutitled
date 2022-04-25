import requests

# UA伪装：user-agent(请求载体的身份标识)
if __name__ == "__main__":
    kw = input("enter a word:")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }
    url = "https://www.sogou.com/web?"
    # 处理url携带的参数：封装到字典中
    param = {
        "query": kw
    }
    res = requests.get(url=url, params=param, headers=headers)
    page_text = res.text
    fileName = kw + '.html'
    with open(file=fileName, mode='w', encoding='utf-8') as f:
        f.write(page_text)
