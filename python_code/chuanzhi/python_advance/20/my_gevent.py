#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : my_gevent.py
# @Author: ly
# @Date  : 2018/12/9


import time
import gevent
from gevent import monkey


def work1(no):
    while True:
        print('work1', no)
        time.sleep(0.5)


def work2(no):
    while True:
        print('work2', no)
        time.sleep(0.5)


if __name__ == '__main__':
    monkey.patch_all()
    g1 = gevent.spawn(work1, 1)
    g2 = gevent.spawn(work2, 2)

    gevent.joinall(g1, g2)





