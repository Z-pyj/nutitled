import requests
import json

if __name__ == '__main__':
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    datas = {
        'cname': '',
        'pid': '',
        'keyword': '杭州',
        'pageIndex': 1,
        'pageSize': 10
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }

    res_text = requests.get(url=url, headers=header, data=datas)
    print(res_text)
    res_json = res_text.json()

    fp = open("./kfc.json", mode='w', encoding='utf-8')

    json.dump(res_json, fp, ensure_ascii=False)

    print("over!!!")

