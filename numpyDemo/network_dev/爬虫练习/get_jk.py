import requests
import time
import json


def get_text_between(txt, left, right):
    num1 = txt.index(left) + len(left)  # index查找字符所在位置
    num2 = txt.index(right)  # len取字符长度
    w_return = txt[num1:num2]  # 取txt区间的字符数据
    return w_return


def get_url(url):
    try:
        r = requests.get(url, params="", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '})
        r.raise_for_status()
        # 转码
        r.encoding = 'utf-8'
        return r.text
    except:
        print("Failed!")


def get_jk_img(jk_item_id):
    try:
        url = "https://bcy.net/item/detail/" + jk_item_id + "?_source_page=hashtag"
        r = requests.get(url, params="", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '})
        r.raise_for_status()
        r.encoding = 'utf-8'
        fanhui = get_text_between(r.text, 'JSON.parse("', '");')
        return fanhui
    except:
        print("Failed!")


def get_jk_data():
    # url = "https://bcy.net/apiv3/common/circleFeed?circle_id=492&since=" + str(int(time.time())) + ".000000&sort_type=2&grid_type=10&_signature=UCWcwAAgEByiCq6HuAav5VAlnNAAA-T"
    # 上面的链接是获取最新的，下面的好像是推荐内容的
    url = "https://bcy.net/apiv3/common/circleFeed?circle_id=492"

    # 获取网页数据
    jk_json = get_url(url)
    # 解码json，转成字典
    jk = json.loads(jk_json)
    # 取jk数目
    jk_num = len(jk['data']['items'])

    data = {}
    for i in range(0, jk_num):
        data_ = {}
        jk_item_id = jk['data']['items'][i]['item_detail']['item_id']  # 文章id
        a = get_jk_img(jk_item_id).replace(r'\"', r'"')
        img_json = json.loads(get_jk_img(jk_item_id).replace(r'\"', r'"'))  # jk图片的json
        img_num = len(img_json['detail']['post_data']['multi'])  # jk图片的数量
        dataimg = {}
        for i2 in range(0, img_num):
            # jk图片链接
            img_url = img_json['detail']['post_data']['multi'][i2]['path'].encode('utf-8').decode("unicode_escape")
            dataimg[i2] = img_url

        jk_plain = jk['data']['items'][i]['item_detail']['plain']  # 文章标题
        data_[0] = jk_item_id
        data_[1] = jk_plain
        data_[2] = dataimg
        data[len(data)] = data_

    return data


if __name__ == '__main__':
    data = get_jk_data()
    print(json.dumps(data))
