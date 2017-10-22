# -*- coding:utf-8 -*-
from regular_random.config import constants
import MySQLdb

mysql_instance = MySQLdb.connect(**constants.MYSQL_DEFINE)
cursor = mysql_instance.cursor()


def regular_model(
        _data,
        col_7,
        period,
        col_permutation_order,
        col_combination_order,
        issue_number,
        total_money,
        first_prize_count,
        first_prize_province,
        second_prize_count):
    SQL = '''INSERT INTO `regular`
            (`pub_time`, `col1`, `col2`, `col3`, `col4`, `col5`, `col6`, `col7`, `permutation_order`, `combination_order`, `issue_number`, `total_money`, `first_prize_count`, `first_prize_province`, `second_prize_count`)
            VALUES ("%s", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "%s", %s)''' % (period,
                                                                                          _data[0],
                                                                                          _data[1],
                                                                                          _data[2],
                                                                                          _data[3],
                                                                                          _data[4],
                                                                                          _data[5],
                                                                                          col_7,
                                                                                          col_permutation_order,
                                                                                          col_combination_order,
                                                                                          issue_number,
                                                                                          total_money,
                                                                                          first_prize_count,
                                                                                          first_prize_province,
                                                                                          second_prize_count)
    cursor.execute(SQL)
    mysql_instance.commit()
