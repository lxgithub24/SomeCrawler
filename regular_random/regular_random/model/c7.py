# -*- coding:utf-8 -*-
import MySQLdb
import copy
from regular_random.config import constants

mysql_instance = MySQLdb.connect(**constants.MYSQL_DEFINE)
cursor = mysql_instance.cursor()
PREDICT_NUM_PREFIX = 10


# 每一期第七列的列表
def get_c7():
    SQL = '''SELECT `col7` FROM `regular`'''
    cursor.execute(SQL)
    results = cursor.fetchall()
    c7_list = []
    for res in results:
        c7_list.append(int(res[0]))
    return c7_list


def cal_rate_list():
    c7_list = get_c7()
    current_issue_count = []
    single_issue = [0 for i in range(16)]
    for i in range(len(c7_list)):
        single_issue[c7_list[i] - 1] += 1
        current_issue_count.append(copy.deepcopy(single_issue))
    return current_issue_count


# 每期公布之后，到目前为止的第七列每个值总排序
def cal_issue_rate():
    def _rank(current_issue):
        sorted_current_issue = sorted(current_issue)
        sorted_issue_dict = {}
        for i in range(len(sorted_current_issue)):
            key = sorted_current_issue[i]
            value = i
            if i != 0 and key == sorted_current_issue[i - 1]:
                value = sorted_issue_dict[sorted_current_issue[i - 1]]
            sorted_issue_dict[key] = value
        issue_rank = [sorted_issue_dict[i] for i in current_issue]
        return issue_rank

    current_issue_count = cal_rate_list()
    issue_rank_list = []
    for current_issue in current_issue_count:
        issue_rank = _rank(current_issue)
        issue_rank_list.append(copy.deepcopy(issue_rank))
    return issue_rank_list


# 下一期属于预测列表中第几名
def next_c7_rank_in_pre():
    c7_list = get_c7()
    issue_rank_list = cal_issue_rate()
    pre_rank = []
    for i in range(1, len(c7_list)):
        curr_rank = issue_rank_list[i - 1][c7_list[i] - 1]
        pre_rank.append(curr_rank)
    print pre_rank
    return pre_rank


if __name__ == '__main__':
    # c7_list = get_c7()
    # print c7_list
    # current_issue_count = cal_rate_list()
    # print current_issue_count
    # issue_rank_list = cal_issue_rate()
    # print issue_rank_list
    # print issue_rank_list
    pre_rank = next_c7_rank_in_pre()
    print sum(pre_rank) / (1. * len(pre_rank))


    # print len(predict_list)
    # print predict_list
