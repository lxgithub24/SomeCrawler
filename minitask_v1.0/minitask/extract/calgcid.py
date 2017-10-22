# -*- coding:utf-8 -*-
import os
from hashlib import sha1
from ..core import constants


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
    f = open(filename, 'rb')
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


if __name__ == '__main__':
    calc_bcid_gcid('{}/1.flv'.format(constants.WORKING_DIRECTORY))
