#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : sql_dua.py
# @Author: ly
# @Date  : 2018/12/21

from pymysql import *
import random

if __name__ == '__main__':
    db = Connection(host="localhost", port=3306,  user='root', password = '111111', charset='utf8', database = 'spider')
    cursor = db.cursor()
    sql = '''insert into spider value(0, 'jijang', 'www.baidu.com')'''
    try:
        for i in range(10):
            res = cursor.execute(sql)
        if random.randint(3, 5) == 3:
            raise Exception('miss exception')
    except Exception as e:
        print('处理了异常')
        # db.rollback()
    else:
        print('无异常正常提交')
        db.commit()
    finally:
        cursor.close()
        db.close()

