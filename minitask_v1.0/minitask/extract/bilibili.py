# -*- coding:utf-8 -*-
import re
import requests
from ..downloader import get_video
from ..models import mysql_model
from ..core import constants
import time


def extract():
    # for item in constants.UPPER_LIST:
    url = 'https://search.bilibili.com/all?keyword=%E8%B0%B7%E9%98%BF%E8%8E%AB&page=1&order=totalrank'
    response = requests.get(url).text
    rcontent = '<li class="video matrix ">(.*?)</li>'
    lists = re.findall(rcontent, response, re.S)
    video_dict = {}
    i = 0
    j = 0
    for list in lists:
        # print(i)
        i += 1
        if i == 3:
            return False
        rsite_src = '<a href="//(.*?)"  target="_blank"'
        site_src = re.findall(rsite_src, list, re.S)[0].strip().replace('amp;','')
        rdescription = '<a class="title"  title="(.*?)" href="'
        description = re.findall(rdescription, list, re.S)[0].strip().replace('amp;','')
        rplaytime = '<i class="icon-playtime" ></i>(.*?)</span>'
        plays = re.findall(rplaytime, list, re.S)[0].strip().replace('amp;','')
        if '万' in plays:
            plays = int(float(plays.replace('万', '')) * 10000)
        rcreatetime = '<i class="icon-date"></i>(.*?)</span>'
        createtime = re.findall(rcreatetime, list, re.S)[0].strip().replace('amp;','')
        if '分钟前' in createtime:
            createtime = int(time.time())
            createtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(createtime))
        elif '小时前' in createtime:
            createtime = int(time.time() - 3600 *
                             int(createtime.replace('小时前', '')))
            createtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(createtime))
        elif '天前' in createtime:
            createtime = int(time.time()) - 3600 * 24 * \
                int(createtime.replace('天前', ''))
            createtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(createtime))
        elif len(createtime) == 5:
            createtime = '2017-' + createtime + ' 00:00:00'
            # createtime = int(
            #     time.mktime(
            #         time.strptime(
            #             createtime,
            #             '%Y-%m-%d %H:%M:%S')))
        else:
            createtime = createtime + ' 00:00:00'
            # createtime = int(
            #     time.mktime(
            #         time.strptime(
            #             createtime,
            #             '%Y-%m-%d %H:%M:%S')))
        rupper = '_up">(.*?)</a>'
        upper = re.findall(rupper, list, re.S)[0].strip().replace('amp;','')
        rduration = '<span class="so-imgTag_rb">(.*?)</span>'
        duration = re.findall(rduration, list, re.S)[0].strip().replace('amp;','')
        if ':' in duration:
            dur = duration.split(':')
            duration = int(dur[0]) * 60 + int(dur[1])
        rpic = 'data-src="//(.*?)" data-loaded="'
        pic = re.findall(rpic, list, re.S)[0].strip().replace('amp;','')
        video_dict = {
            'site_src': site_src,
            'description': description,
            'plays': plays,
            'create_time': createtime,
            'upper': upper,
            'duration': duration,
            'pic': pic,
            'mov':j
        }
        # print('video_dict(without mov) is\n{}'.format(video_dict))
        video_dict = get_video.download(video_dict,j)
        # print('video_dict(with mov) is\n{}'.format(video_dict))
        mysql_model.crawler_into_db(video_dict)
        j = j + 1
        # print(video_dict)
    return video_dict


if __name__ == '__main__':
    extract()
