# -*- coding:utf-8 -*-
import requests
from classfied_search.model import ORM
import re
import json
import hashlib


#url 'http://gaokao.eol.cn/html/g/mingdan/'
# 爬取各省的所有大学
def get_college_provice_list():
    res_dict = {'大学': {}}
    url = 'http://gaokao.eol.cn/html/g/mingdan/'
    urlmd5 = hashlib.md5(url).hexdigest()
    req = requests.get(url)
    req.encoding = 'gb2312'
    req = req.text.encode('utf8')
    rcontent = '<tbody>(.*?)</tbody>'
    _table = re.findall(rcontent, req, re.S)[0]
    rcontent = '<td>(.*?)<a href="'
    provice = re.findall(rcontent, _table, re.S)
    rcontent = '<a href="(.*?)">'
    provice_url = re.findall(rcontent, _table, re.S)
    for i in range(len(provice)):
        key = provice[i].replace('\n', '')
        value = provice_url[i].replace('\n', '')
        res_dict['大学'].update({key: value})
    for k, v in res_dict['大学'].iteritems():
        req = requests.get(v)
        req.encoding = 'gb2312'
        req = req.text.encode('utf8')
        rcontent = '<tbody>(.*?)</tbody>'
        req = re.findall(rcontent, req, re.S)[0]
        rcontent = '<tr>(.*?)</tr>'
        req = re.findall(rcontent, req, re.S)[3:]
        college_list = []
        for college in req:
            college_info = {}
            rcontent = '<td>(.*?)</td>'
            req = re.findall(rcontent, college, re.S)
            if len(req) == 0:
                continue
            college_info['序号'] = req[0].replace('\n', '')
            college_info['学校名称'] = req[1].replace('\n', '')
            college_info['学校标识码'] = req[2].replace('\n', '')
            college_info['主管部门'] = req[3].replace('\n', '')
            if len(req) == 7:
                college_info['所在地'] = req[4].replace('\n', '')
                college_info['办学层次'] = req[5].replace('\n', '')
                college_info['备注'] = req[6].replace('\n', '')
            else:
                college_info['备注'] = req[4].replace('\n', '')
            college_list.append(college_info)
        res_dict['大学'][k] = {v: college_list}
    SQL_dict = {"url": url, "urlmd5": urlmd5, "info": res_dict}
    print SQL_dict
    ORM.College_info.add(SQL_dict)
    res_dict = json.dumps(res_dict, encoding='utf8', ensure_ascii=False)
    print (res_dict)


def get_college_info_mysql():
    json_res = ORM.College_info.query(2).info
    return json.dumps(json_res, ensure_ascii=False)


if __name__ == '__main__':
    # get_college_provice_list()
    print get_college_info_mysql()