import requests
import json
import logging
import time
requests.packages.urllib3.disable_warnings()
url = 'https://testapi.ydl.com/api/smart-rank/v1/search'
json_date = {
    "fields": {
        "doctor_id": 'true',
        "doctor_name": 'true',
        "uid": 'true',
        "gender": 'true',
        "chat_status": 'true',
        "booking_status": 'true',
        "consult_status": 'true',
        "listen_status": 'true',
        "years": 'true',
        "head": 'true',
        "province": 'true',
        "city": 'true',
        "evaluation_average_score": 'true',
        "evaluate_num": 'true',
        "min_price": 'true',
        "title": 'true',
        "titles.title": 'true',
        "famous_remark": 'true',
        "help_num": 'true',
        "p30d_sold_hour": 'true',
        "sum_service_time": 'true',
        "doctor_products": 'true',
        "product_cates": 'true',
        "product_specs": 'true',
        "icons": 'true',
        "link_url": 'true',
        "has_servicefree_consult": 'true',
        "is_new_enter": 'true',
        "consult_final_score": 'true',
        "ability_level": 'true',
        "chat_btn_text": 'true',
        "feature_tags": 'true',
        "open_chat_agency": 'true',
        "service_status": 'true',
        "is_free_today": 'true'
    },
    "filter": {},
    "sorts": {
        "general": -1
    },
    "options": {
        "search_scene_id": "doctor_main_search",
        "extras": {
            "skips": {
                "726617832470364160": 11,
                "726617832470364161": 9,
                "skip": 20
            }
        },
        "ffrom": "m",
        "uid": "0"
    }
}
res = requests.post(url, json=json_date, verify=False)
print(res.json())
