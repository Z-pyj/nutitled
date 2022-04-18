import requests
import json
import os
import re

if __name__ == '__main__':
    url = "http://jandan.net/top"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }

    res_text = requests.get(url=url, headers=headers).text
    img_src_list = re.findall("", res_text, re.S)
