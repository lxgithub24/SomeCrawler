import requests
import re
import os
from hashlib import sha1
import subprocess
import sys
sys.path.append('..')
from minitask.core import constants
# from minitask.extract import calgcid
import pymysql
import zlib

# def dbcon():
#     con = pymysql.connect(constants.HOST,'root','liuxiang','video_info')
#     cursor = con.cursor()
#     return cursor


def test_response():
    url = 'https://search.bilibili.com/all?keyword=%E8%B0%B7%E9%98%BF%E8%8E%AB&page=1&order=totalrank'
    response = requests.get(url).text
    rcontent = '<li class="video matrix ">(.*?)</li>'
    lists = re.findall(rcontent, response, re.S)
    print(lists[2])
    # print(len(lists)


def calc_block_size(filesize):
    if filesize >= 0 and filesize <= (128 << 20):
        return 256 << 10
    elif filesize > (128 << 20) and filesize <= (256 << 20):
        return 512 << 10
    elif filesize > (256 << 20) and filesize <= (512 << 20):
        return 1024 << 10
    else:
        return 2048 << 10


def calc_bcid_gcid(filename):
    fstat = os.stat(filename)
    filesize = fstat.st_size
    f = open(filename, 'r')
    # f = open(filename, 'rb')
    block_size = calc_block_size(filesize)
    block_number = (filesize + block_size - 1) / block_size
    sha_g = sha1()
    total = 0
    bcid = ""
    for i in range(int(block_number)):
        sha_b = sha1()
        need = 0
        if i != (block_number - 1):
            need = block_size
        else:
            need = filesize % block_size
        buf = f.read(need)
        total += need
        # sha_b.update(buf.encode())
        sha_b.update(buf)
        outbuffer = sha_b.digest()
        bcid += str(outbuffer)
        sha_g.update(outbuffer)
    gcid = sha_g.hexdigest()
    return gcid


def opcmd():
    p = subprocess.Popen(
        'mv {}/guamo.flv {}/1.flv'.format(
            constants.WORKING_DIRECTORY,
            constants.WORKING_DIRECTORY),
        shell=True)
    # p.wait()


def sqlalchem():
    con = pymysql.connect(constants.HOST, 'root', 'liuxiang', 'minitask')
    cursor = con.cursor()
    SQL = '''INSERT INTO `video_info`(`pic`,`mov`,`description`,
`plays`,`create_time`,`upper`,`duration`,`site_src`) VALUES('1','1','%1s',1,1212121212,'%2s',1,'%1s')'''
    try:
        print(SQL)
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        print(id)
        print(111111)
        return True
    except:
        print(22222222)
        return False

# def openfile():
#     filepath = '/home/liuxianga/test/download_bilibili/1.mp4'
    # f = open('temp.txt', 'r',encoding='utf-8')

if __name__ == '__main__':
    # test_response()
    print(calc_bcid_gcid('/home/liuxianga/test/download_bilibili/1.mp4'))
    # opcmd()
    # sqlalchem()