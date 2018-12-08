#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : process.py
# @Author: ly
# @Date  : 2018/12/8


import multiprocessing
import os
import time

i = 0


def c_process_func(name, play):
    global i
    i += 1000


def main():
    """单进程 单线程 之前写的代码在主线程上"""
    c_p = multiprocessing.Process(target=c_process_func, args=('zhaobenshan',), kwargs={'play':'xiaopin'})
    c_p.start()
    c_p.join()
    print('子线程改 i 的值后, 主线程取i的值为 %s' % i)


if __name__ == '__main__':
    main()
