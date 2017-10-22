# -*- coding:utf-8 -*-
from ..core import constants
import pymysql
from ..models.ORM import Video_info


def crawler_into_db(video_dict):
    Video_info.add(video_dict)
#     conn = pymysql.connect(
#         constants.HOST,
#         constants.USER,
#         constants.PWD,
#         constants.DB)
#     cursor = conn.cursor()
#
#     SQL = '''INSERT INTO `video_info`(`pic`,`mov`,`description`,`plays`,`create_time`,`upper`,`duration`,`site_src`) VALUES("%s",%d,"%s",%d,"%s","%s",%d,"%s")''' % (str(video_dict.get('pic')), int(
#         video_dict.get('mov')),str(video_dict.get('description')), int(video_dict.get('plays')), str(video_dict.get('create_time')), str(video_dict.get('upper')), int(video_dict.get('duration')), str(video_dict.get('site_src')))
#     SQL = '''INSERT INTO `video_info`(`pic`,`mov`,`description`,`plays`,`create_time`,`upper`,`duration`,`site_src`) VALUES(
# "i0.hdslb.com/bfs/archive/1882297a1cd9ffed5cf527dcf40bb716b69ecd8d.jpg",0,"【谷阿莫】5分鐘看完2017男性器官治療師的電影《性感尤物 Sex Doll》",390000,"2017-08-10 00:00:00","谷阿莫",359,"www.bilibili.com/video/av13199912?from=search&seid=6342520915173201508")'''
#     print(SQL)
#     try:
#         print(0)
#         cursor.execute(SQL)
#         cursor.close()
#         conn.close()
#         print(1)
#         conn.commit()
#         print("insert success")
#     except BaseException:
#         print("insert failed")
