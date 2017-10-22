# -*- coding:utf-8 -*-
import requests
from lxml import html
import re

from regular_random.controller import cal_order
START_INDEX = 1
END_INDEX = 110


def get_basic_info():
    for i in range(START_INDEX, END_INDEX):
        print i
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_{}.html'.format(
            str(i))
        response = requests.get(url).text
        response = html.fromstring(response)
        issue_lists = response.xpath('//tr')[2:-1]
        for issue in issue_lists:
            res = issue.xpath('./td')
            pub_time = res[0].text + ' 21:30:00'
            issue_number = res[1].text
            res_data = res[2].xpath('./em/text()')
            _data = []
            for res_ in res_data:
                _data.append(int(res_))
            total_money = res[3].xpath('./strong')[0].text.replace(',', '')
            first_prize_count = res[4].xpath('./strong')[0].text
            first_prize_province = res[4].xpath(
                './text()')[0].encode('utf8').replace('\r', '').replace('\n', '').strip()
            second_prize_count = res[5].xpath('./strong')[0].text
            # print
            # pub_time,issue_number,_data,total_money,first_prize_province,first_prize_count,second_prize_count
            cal_order.cal_order(_data[:-1],
                                pub_time,
                                _data[6],
                                issue_number,
                                total_money,
                                first_prize_count,
                                first_prize_province,
                                second_prize_count)


if __name__ == '__main__':
    get_basic_info()
