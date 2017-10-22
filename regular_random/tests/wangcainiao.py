# -*- coding:utf-8 -*-
url_real = 'https://item.jd.com/11263863972.html'
url_wangcainiao = 'https://s.m.taobao.com/h5?q=%E6%B3%95%E8%AF%BA%E5%A8%81%E5%B9%B3%E8%A1%A1%E8%BD%A6&nid_up=11263863972'
url_wcn_key = '老年男装'
url_wcn_value = 'https://s.m.taobao.com/h5?q=%E8%80%81%E5%B9%B4%E7%94%B7%E8%A3%85&nid_up=558650254029'
url_wcn_zh_value = 'https://s.m.taobao.com/h5?q=老年男装&nid_up=558650254029'

url_lx_key = '花花公子正装鞋'
url_lx_jd = 'https://item.jd.com/3485582.html'

import urllib

def gen_url(key, id_):
    key = urllib.quote(key)
    return 'https://s.m.taobao.com/h5?q={}&nid_up={}'.format(key,str(id_))



# url_1 = gen_url('老年男装', 558650254029)
# print url_1



import qrcode

data = 'http://write.blog.csdn.net/'
img_file = r'D:\py_qrcode.png'

img = qrcode.make(data)
# 图片数据保存至本地文件
img.save(img_file)
# 显示二维码图片
img.show()


# answer
# 淘宝
# https://s.m.taobao.com/h5?q=老年男装&nid_up=558650254029

# 京东
#