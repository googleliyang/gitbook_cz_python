#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : process.py
# @Author: ly
# @Date  : 2018/12/8


import multiprocessing
import os
import time


def c_process_func(name, play):
    while True:
        print('我是子进程, 我叫 %s \n' % name)
        time.sleep(1)
    # print('我是子进程，我的父id 是 %s' % os.getppid())


def main():
    """单进程 单线程 之前写的代码在主线程上"""
    for i in range(5):
        c_p = multiprocessing.Process(target=c_process_func, args=('zhaobenshan'+str(i),), kwargs={'play':'xiaopin'})
        c_p.start()


if __name__ == '__main__':
    main()
