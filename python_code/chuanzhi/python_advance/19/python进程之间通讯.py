#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : python进程之间通讯.py
# @Author: ly
# @Date  : 2018/12/8

import multiprocessing
import time


def get_data(q):
    """子进程入口"""
    while True:
        if q.empty():
            print('队列是空的，一会再来看看')
            time.sleep(5)
        else:
            print('获取到的数据是%s' % q.get())
            time.sleep(2)


if __name__ == '__main__':
    q = multiprocessing.Queue(1000)
    c_p = multiprocessing.Process(target=get_data, args=(q,))
    c_p.start()
    while True:
        val = input("请输入")
        if q.full():
            print('客官已经满了，请稍后再来')
            time.sleep(1)
        else:
            q.put(val)

