import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36 '
    }
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储企业所有的详情数据
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 参数的封装
    for page in range(1, 15):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        text_res = requests.post(url=url, headers=headers, data=data)
        print(text_res)
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        # 从 json_ids 字典中拿到 list 对应的 value 值，对 value 值列表进行遍历
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        # print(id_list,'\n')

    # 获取企业详情数据,也是动态加载出来的，携带一个参数 id，其值可以通过前一步生成的 id列表提取
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }

        json_detail = requests.post(url=post_url, data=data, headers=headers).json()
        # print(json_detail, '-------------END----------')
        all_data_list.append(json_detail)
        all_data_list.append('---------------------------------------------------------')

    # 持久化存储all_data_list
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False, indent=True)  # indent 自动排版
    print('Over!')
