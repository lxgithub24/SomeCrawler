# -*- coding:utf-8 -*-
import requests
import hashlib
import re
import logging
import json
from classfied_search.model import ORM
logging.basicConfig(filename='travel_info_10140020.log', level=logging.INFO, format='')


# url http://you.ctrip.com/sitemap/spotdis/c0
# 携程旅游网站的各地旅游经典信息
def get_travel_info():
    url = 'http://you.ctrip.com/sitemap/spotdis/c0'
    urlmd5 = hashlib.md5(url).hexdigest()
    req = requests.get(url)
    req.encoding = 'utf8'
    req = req.text
    rcontent = '''<div class="sitemap_block">(.*?)</ul>'''
    province_list = re.findall(rcontent, req, re.S)
    travel_info_value = []
    travel_info = {"中国":travel_info_value}
    for province in province_list:
        print 'province', province
        logging.info(province)
        province_dict = {}
        rcontent = '<h2>(.*?)</h2>'
        province_name = re.findall(rcontent, province, re.S)[0].encode('utf8').replace('\r\n', '').replace(' ', '')
        rcontent = u'''class="more" href="(.*?)">{}</a>'''.format(u'更多')
        province_url = re.findall(rcontent, province, re.S)
        if len(province_url) == 0:
            province_url = ''
        else:
            province_url = province_url[0]
        if isinstance(province_url, unicode):
            province_url.encode('utf8')
        rcontent = '''title="(.*?)" href="'''
        city_name_list = re.findall(rcontent, province, re.S)
        rcontent = '''href="http://(.*?)">'''
        city_url_list = re.findall(rcontent, province, re.S)
        site_list = []
        for i in range(len(city_name_list)):
            print i
            site_dict = {}
            city_url = city_url_list[i]
            logging.info(city_name_list[i])
            city_url_kv = {}
            for j in range(1, 1000):
                if 'http://' not in city_url:
                    city_url = 'http://' + city_url
                url = city_url.replace('.html', '/s0-p{}.html#sightname'.format(str(j)))
                req = requests.get(url)
                req = req.text
                rcontent = '<div class="rdetailbox">(.*?)</p>'
                page_list = re.findall(rcontent, req, re.S)
                if len(page_list) == 0:
                    break
                city_url_value = []

                for block_list in page_list:
                    scenic_info_dict = {}
                    rcontent = '''<a target="_blank" href="(.*?)" title="'''
                    scenic_url = re.findall(rcontent, block_list, re.S)
                    scenic_info_dict['scenic_url'] = scenic_url
                    rcontent = '''title="(.*?)">'''
                    scenic_name = re.findall(rcontent, block_list, re.S)
                    scenic_info_dict['scenic_name'] = scenic_name
                    rcontent = '''<s >(.*?)</s>'''
                    scenic_rank = re.findall(rcontent, block_list, re.S)
                    scenic_info_dict['scenic_rank'] = scenic_rank
                    rcontent = '''class="ellipsis">(.*?)</dd>'''
                    scenic_place = re.findall(rcontent, block_list, re.S)
                    if scenic_place:
                        scenic_place = scenic_place[0].replace('\r', '').replace('\n', '').replace(' ', '')
                        scenic_info_dict['scenic_place'] = scenic_place
                    city_url_value.append(scenic_info_dict)
                city_url_kv[city_url] = city_url_value
            site_dict[city_name_list[i]] = city_url_kv
            site_list.append(site_dict)
        province_url_dict = {}
        province_url_dict[province_url] = site_list
        province_dict[province_name] = province_url_dict
        travel_info_value.append(province_dict)
    SQL_dict = {"url": url, "urlmd5": urlmd5, "info": travel_info}
    ORM.College_info.add(SQL_dict)
    with open('travel_info', 'w') as f:
        f.write(json.dumps(travel_info))


def get_travel_info_mysql():
    return json.dumps(ORM.College_info.query(3).info, ensure_ascii=False)


if __name__ == '__main__':
    # get_travel_info()
    print get_travel_info_mysql()