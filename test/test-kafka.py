# -*- coding:utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

# kafkaconn = {
#         'tw07a121': '9092',
#         'tw07a122': '9092',
#         'tw07a123': '9092',
#         'tw07a124': '9092',
#         'tw07a125': '9092'}

kafkaconn = {'127.0.0.1': 9092}


class Kafka_producer():
    '''
    使用kafka的生产模块
    '''

    def __init__(self, kafkatopic, **kafkaconn):
        self.kafkaconn = kafkaconn
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers=kafkaconn)

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print e

    def sendstringdata(self, params):
        try:
            producer = self.producer
            producer.send(self.kafkatopic, params.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print e


class Kafka_consumer():
    '''
    使用Kafka—python的消费模块
    '''

    def __init__(self, kafkatopic, groupid, **kafkaconn):
        self.kafkaHost = kafkaconn
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(
            self.kafkatopic,
            group_id=self.groupid,
            bootstrap_servers=kafkaconn)

    def consume_data(self):
        try:
            print '##-_-##', self.consumer
            message = self.consumer
            # for message in self.consumer:
            print '??-_-??', message
            # yield message
        except KeyboardInterrupt as e:
            print e


def main():
    '''
    测试consumer和producer
    :return:
    '''
    # 测试生产模块

    producer = Kafka_producer(kafkatopic="rio-strange", kafkaconn=kafkaconn)
    print kafkaconn
    params = 'website_data_upload\t1500626999757\id = 1, url = http://www.baidu.com, title =1, pic =1, status =1, create_time =1, language =, moviename =, director =, brief_infoduction =, tags =1'
    # params = params
    print params
    producer.sendstringdata(params)
    # 测试消费模块
    # 消费模块的返回格式为ConsumerRecord(topic=u'ranktest', partition=0, offset=202, timestamp=None,
    # \timestamp_type=None, key=None, value='"{abetst}:{null}---0"', checksum=-1868164195,
    # \serialized_key_size=-1, serialized_value_size=21)
    consumer = Kafka_consumer(
        kafkatopic='rio-strange',
        groupid='hiang-rio-strange',
        kafkaconn=kafkaconn)
    message = consumer.consume_data()
    print 'message#', message


if __name__ == '__main__':
    main()
