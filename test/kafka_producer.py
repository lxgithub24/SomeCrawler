# -*- coding:utf-8 -*-
import multiprocessing
import time
from kafka import KafkaProducer


def worker(ch):
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

    for i in range(10):
        time.sleep(0.01)
        print 'produce msg', i
        producer.send('publish_msg', ch * 1024)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker, args=('1',))
    p2 = multiprocessing.Process(target=worker, args=('2',))
    p1.start()
    p2.start()