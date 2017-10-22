from tests import TestCase
from functools import reduce
from operator import add
import json
import datetime


class TestPushApi(TestCase):

    def register_user(self, uid):
        data = dict(data=dict(
            peerid='12345',
            uid=uid, 
            services_id='12345a67',
            status='1',
            detail='so fucking details',
            pusher='getui',
            tags=['default'],
            time=str(datetime.datetime.now())
        ))
        resp, status, header = self.request(
            path='/push_services/peer/register/',
            method='POST', data=json.dumps(data))
        res = reduce(add, map(bytes, resp)).decode()
        return json.loads(res)

    def test_async_singlecast(self):
        uid = '123456'
        self.register_user(uid)

        data = {
            'msg': {
                'title': 'xxxx',
                'body': 'xxxx',
                'extras': {}
            },
            'sid': [uid],
            'type': 'uid',
            'delay': '2',
            'async': '1'
        }
        resp, status, header = self.request(
            path='/push_services/admin/push/singlecast/',
            method='POST', data=json.dumps(data))
        res = reduce(add, map(bytes, resp)).decode()
        print(res)
        self.assertEqual(json.loads(res)['result'], 'ok')
        resp, status, header = self.request(
            path='/push_services/admin/push/singlecast/',
            method='POST', data=json.dumps([data, data, data, data]))
        res = reduce(add, map(bytes, resp)).decode()
        self.assertEqual(json.loads(res)['result'], 'ok')