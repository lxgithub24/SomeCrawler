# -*- coding:utf-8 -*-
import urllib
import sys

url = 'http://search.jd.com/Search?keyword=%s&enc=utf-8'


def gen_url(key_, id_):
    key_ = urllib.quote(key_)
    return 'https://s.m.taobao.com/h5?q={}&nid_up={}'.format(key_, str(id_))


if __name__ == '__main__':
    key_ = sys.argv[1]
    id_ = sys.argv[2]
    url_1 = gen_url(key_, id_)
    print url_1
