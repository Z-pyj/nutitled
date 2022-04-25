import requests
import json

if __name__ == "__main__":
    kw = input("enter a word:")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }
    url = "https://fanyi.baidu.com/sug"
    # post请求携带的参数data，封装到字典中
    data = {
        "kw": kw
    }
    # 发起请求
    res = requests.post(url=url, headers=headers, data=data)
    # 获取响应结果转为json格式
    res_json = res.json()
    # 数据持久化
    fp = open("fanyi.json", mode='w', encoding='utf-8')
    json.dump(res_json, fp=fp, ensure_ascii=False)
    print("抓取完成")
