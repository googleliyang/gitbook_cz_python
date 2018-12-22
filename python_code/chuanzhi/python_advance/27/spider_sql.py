#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : spider_tabtang.py
# @Author: ly
# @Date  : 2018/12/16


import re
import os
import time
import threading
import urllib.request
from pymysql import connect


class Db:
    def __init__(self):
        self.db_connect = connect(host='localhost', port=3306, database='spider', user='root', password='111111',
                             charset='utf8')
        self.cursor = self.db_connect.cursor()
        # self.cursor.execute('create table spider')

    def exec(self, sql, args = None):
        self.cursor.execute(sql, args)
        if args:
            self.db_connect.commit()
        else:
            res = self.cursor.fetchall()
            return res

class Spider:
    # 初始化方法
    def __init__(self, db):
        self.db = db
        # 定义字典, 保存下载名和地址
        self.film_links = {}
        # 因为使用多线程实现多任务，所以需要一把互斥锁
        self.lock = threading.Lock()
        self.i = 1

    # 定义一个多任务的工作函数
    def down_task(self, page):
        print('*'*20 + '新线程开始处理' + str(page) + '*' * 20)
        list_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_%d.html' % page
        # 默认使用 tcp 方式
        list_res = urllib.request.urlopen(list_url)
        # 使用 socket 读取获取页面数据并转码(源文件是什么编码，解码时便用什么)
        list_content = list_res.read(10<<20).decode('GBK')

        # 通过 findall 方法将内容列表中所有的下载页提取出来
        # <a href="/html/gndy/dyzz/20181129/57853.html" class="ulink">2018年动作《功夫联盟》HD国粤双语中字</a>
        # <a href="(.*)" class="ulink">.*</a>
        film_list = re.findall(r'<a href="(.*)" class="ulink">(.*)</a>', list_content)
        # print('取得的数据为', film_list)
        # 遍历列表 拼接地址 读取内容
        for i in film_list:
            # 拼接地址
            download_url = 'http://www.dytt8.net' + i[0]
            # print(download_url)
            res = urllib.request.urlopen(download_url)
            download_content = res.read().decode('GBK')
            #  <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="ftp://ygdy8:ygdy8@yg90.dydytt.net:8432/阳光电影www.ygdy8.com.河流如血.BD.720p.中英双字幕.mkv">ftp://ygdy8:ygdy8@yg90.dydytt.net:8432/阳光电影www.ygdy8.com.河流如血.BD.720p.中英双字幕.mkv</a></td>
            url = re.search(r'bgcolor="#fdfddf"><a href="(.*)"', download_content)
            if url:
                key = i[1]
                value = url.group(1)
                with self.lock:
                    print('当前正在下载电影为 %d 部' % self.i)
                    self.film_links[key] = value
                    print('--'*20, value, key)
                    self.db.exec('insert into spider value(0, %s, %s)', (key, value))
                    self.i += 1
                    print('电影名为 %s 地址为 %s' % (key, value))

            # print(url.group(1))
            # 还是用 join 吧

    def run(self):
        # 多线程下载 实现多任务下载
        for page in range(1, 2 << 1):
            t = threading.Thread(target=self.down_task, args=(page, ))
            t.start()

        # 循环判断主线程是不是最后一个线程，如果是说明爬取任务完成了
        while len(threading.enumerate()) != 1:
            # 等待爬取
            time.sleep(1)
            pass
            # 查看爬取的结果
        print('='* 100)
        res = self.db.exec('select * from spider')
        print(res)
        for i in res:
            print('query from sql', i)
        self.call_bash()
        # 返回爬取结果写入文件 | 数据库
        return self.film_links

    def call_bash(self):
        # os.system('ls')
        # res = os.popen("ls").read()
        os.system('./test.sh')


def main():
    db = Db()
    spider = Spider(db)
    spider.run()

def test():
    db = Db()
    res = db.exec('select * from spider')
    print(res)
    for i in res:
        print(i)

def test_bash():
    db = Db()
    spider = Spider(db)
    spider.call_bash()


if __name__ == '__main__':
    main()
    #test()
    # test_bash()
