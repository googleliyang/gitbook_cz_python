#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : deco_pass_param.py
# @Author: ly
# @Date  : 2018/12/15

import time


def record_time(params):

    print('装饰器收到的参数为', params)

    def outer(func):

        def wrapper(*arg, **kwargs):
            start = time.time()
            print('传入参数为 %s', arg)
            func(*arg, **kwargs)
            end = time.time()
            print('函数执行时间为', end - start)
        return wrapper

    print('decorator end')
    return outer


@record_time(123)
def run(no1, no2, no3):
    n = 0
    print('被修饰的函数执行')
    for i in range(10 << 10):
        n += i
    print(n)


run(1, 2, 3)
