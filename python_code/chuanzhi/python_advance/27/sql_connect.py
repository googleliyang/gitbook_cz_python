#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : sql_connect.py
# @Author: ly
# @Date  : 2018/12/21


from pymysql import connect

# 创建数据库链接对象
db_connect = connect(host='localhost', port=3306, database='python_db', user='root', password='111111', charset='utf8')

sql = '''select * from students '''


# 创建游标
cursor = db_connect.cursor()
res = cursor.execute(sql)
print('一共影响力 %d行数据' % res)

print('-'*50 + '查询指定数据' + '-'*50)

res1 = cursor.fetchone()
print(res1)

print('-'*50 + '查询一条数据' + '-'*50)

res2 = cursor.fetchmany(3)
for t in res2:
    print(t)

print('-'*50 + '查询多条数据' + '-'*50)

res1 = cursor.fetchall()
for i in res1:
    print(i)
print('-'*50 + '查询所有数据' + '-'*50)

# 使用游标操作
print(cursor.rowcount)
# 关闭游标
cursor.close()

# 关闭链接
db_connect.close()
