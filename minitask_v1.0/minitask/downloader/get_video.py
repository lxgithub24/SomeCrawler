# -*- coding:utf-8 -*-
from ..extract import bilibili, calgcid
import subprocess
from ..core import constants


def download(video_dict,j):
    site_url = video_dict.get('site_src')
    try:
        getvideo_cmd = 'you-get -O {} --format=mp4 {}'.format(j,site_url)
        print(getvideo_cmd)
        p = subprocess.Popen(
            getvideo_cmd,
            shell=True,
            cwd=constants.WORKING_DIRECTORY)
        # print('11111111111111111111111')
        # print(p.returncode)
        # print('1111111111111111111')
        p.wait()
        # p.wait(600)
        # try:
        #     print(0)
        #     mov = calgcid.calc_bcid_gcid('{}/1.mp4'.format(constants.WORKING_DIRECTORY))
        #     print(1)
        #     change_name = 'mv {}/1.mp4 {}/{}.mp4'.format(
        #         constants.WORKING_DIRECTORY, constants.WORKING_DIRECTORY, mov)
        #     print(2)
        #     subprocess.Popen(change_name, shell=True)
        #     print(3)
        #     video_dict['mov'] = mov
        #     print('video_dict(with mov) is\n{}'.format(video_dict))
        #     return video_dict
        # except BaseException:
        #     print('no 1.mp4 to cal sig & BaseException in')
        # return video_dict
    except BaseException:
        print("download failed & BaseException out")
    return video_dict
