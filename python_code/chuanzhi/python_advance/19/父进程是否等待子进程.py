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
        print('我是子进程, 我叫 %s 我演过 %s 我的 pid 是 %s' % (name, play, multiprocessing.current_process().pid))
        print('我是子进程，我的父id 是 %s' % os.getppid())
        time.sleep(1)


def main():
    """单进程 单线程 之前写的代码在主线程上"""
    c_p = multiprocessing.Process(target=c_process_func, args=('zhaobenshan',), kwargs={'play':'xiaopin'})
    c_p.start()


if __name__ == '__main__':
    main()
