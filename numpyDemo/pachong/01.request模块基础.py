import requests

if __name__ == "__main__":
    # 指定url
    url = "https://www.sogou.com/"
    # 发起请求
    res = requests.get(url=url)
    # 获取响应，text返回字符串格式的数据
    page_text = res.text
    print(page_text)
    with open("sogou.html", mode="w", encoding="utf-8") as f:
        f.write(page_text)
