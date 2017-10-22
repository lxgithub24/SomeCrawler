# -*- coding:utf-8 -*-
import urllib2
import re


def get_html():
    url = 'http://www.80s.tw/top/last_update'
    User_Agent = "Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11"
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    headers = {"User-Agent": User_Agent, "Accept": Accept}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    print html
    return html


def GetMainInfo(html):
    regex = re.compile('<span class="tpsp2">(.*?) </span>', re.S)
    res = regex.findall(html)
    return res


def write_to_file(res_list):
    path = '/home/liuxianga/80s'
    f = open(path, 'w')
    for str in res_list:
        f.writelines(str + '\n')
    f.close()


if __name__ == '__main__':
    html = get_html()
    res_list = GetMainInfo(html)
    write_to_file(res_list)
