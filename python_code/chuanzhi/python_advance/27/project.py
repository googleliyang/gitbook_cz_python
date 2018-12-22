#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : project.py
# @Author: ly
# @Date  : 2018/12/21

from pymysql import *


class JdServer:

    def __init__(self):
        self.exit = False
        self.__db = Connection(host='localhost', port=3306, user='root', password='111111', database='jddb', charset='utf8')
        pass

    # 循环打印菜单
    # 输入需要执行选项的 ID
    def run(self):
        while True:
            print('1: 查询所有商品信息')
            print('2: 查询所以有商品所在种类信息')
            print('3: 查询所以有商品所在品牌信息')
            print('4: 添加商品种类')
            print('5: 根据id查询商品信息')
            print('6: 根据id查询商品信息方式')
            print('7: 退出系统')
            select_id = input('请输入需要操作的id')
            self.select_oper(select_id)
            if self.exit:
                break


    # 实现功能选择函数根据不同id 实现不同函数
    def select_oper(self, select_id):
        print('您要执行的操作是 %s' % select_id)
        select_id = int(select_id)
        if select_id == 1:
            self.show_all_goods_info()
        elif select_id == 2:
            self.show_all_goods_cat()
        elif select_id == 3:
            self.show_all_goods_brand()
            pass
        elif select_id == 4:
            self.add_good()
        elif select_id == 5:
            self.show_detail_goods()
            pass
        elif select_id == 6:
            self.show_detail_good_info()
            pass
        elif select_id == 7:
            self.exit_sys()
            pass
        else:
            print('您输入的有错误')

    def exit_sys(self):
        self.exit = True

    # 可以同时创建多个游标，为了方便，同一时刻让一个游标工作即可
    def show_all_goods_info(self):
        sql_str = ''' select * from goods '''
        self.exec_sql(sql_str)

    def show_all_goods_cat(self):
        sql_str = ''' select goods.id id, goods.name name, goods.cate_id, goods_cates.name from goods left join  goods_cates on goods_cates.id = goods.cate_id'''
        self.exec_sql(sql_str)

    def show_all_goods_brand(self):
        sql_str = ''' select goods.id id, goods.name name, goods.cate_id, goods_brands.name from goods left join  goods_brands on goods_brands.id = goods.cate_id'''
        self.exec_sql(sql_str)

    # 查询 具体id
    def show_detail_goods(self):
        id = input('请输入要查询的商品id')
        sql_str = 'select * from goods where id = %s'
        self.exec_sql(sql_str, (id, ))

    # 5 查询 具体id
    def show_detail_good_info(self):
        id = input('请输入要查询的商品id')
        sql_str = 'select * from goods_brands where id = %s '
        self.exec_sql(sql_str, (id, ))

    def add_good(self):
        good_name = input('输入商品名称')
        c_id = input('请输入种类id')
        b_id = input('请输入品牌id')
        sql_str = '''insert into goods(name, cate_id, brand_id) value(%s, %s, %s)'''
        self.exec_sql(sql_str, (good_name, c_id, b_id))
        self.__db.commit()

    def exec_sql(self, sql, args = None):
        cur = self.__db.cursor()
        try:
            cur.execute(sql, args)
            res = cur.fetchall()
        except Exception as e:
            self.__db.rollback()
        else:
            print('执行成功')
            self.show_result(res)
        finally:
            cur.close()

    # 抽取一个用来显示查询结果的函数
    def show_result(self, res):
        for i in res:
            print(i)
        pass

def main():
    # 创建一个实例对象
    jd_server = JdServer()
    jd_server.run()


if __name__ == '__main__':
    main()
