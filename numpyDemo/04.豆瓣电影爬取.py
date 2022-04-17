import requests
import json

if __name__ == '__main__':
    db_xj_top_url = "https://movie.douban.com/j/chart/top_list"
    param = {
        "type": 24,
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }

    res_text = requests.get(url=db_xj_top_url, params=param, headers=header)
    print(res_text)
    res_json = res_text.json()
    fp = open("./douban.json", mode='w', encoding='utf-8')
    json.dump(res_json, fp=fp, ensure_ascii=False)
    print("over!!!")
