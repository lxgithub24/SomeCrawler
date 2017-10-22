# -*- coding:utf-8 -*-
import requests
import re


def get_info():
    url = 'http://you.ctrip.com/sitemap/spotdis/c0'
    req = requests.get(url)
    req = req.text
    # print req
    rcontent = '''</script>(.*?)'''
    las = re.findall(rcontent, req, re.S)
    print las


if __name__ == '__main__':
    get_info()
