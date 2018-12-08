#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 进程池.py
# @Author: ly
# @Date  : 2018/12/8

import multiprocessing
import os
import time


def test(n):
    for i in range(3):
        print('Pid is %s 打印数字为 %s' % (os.getpid(), n))
        time.sleep(1)


def main():
    pool = multiprocessing.Pool(3)
    pool.apply_async(test, args=(1,))
    pool.apply_async(test, args=(2,))
    pool.apply(test, args=(3, ))
    pool.apply(test, args=(4, ))
    pool.close()
    # pool.join()


if __name__ == '__main__':
    main()

