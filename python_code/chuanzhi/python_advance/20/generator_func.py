#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : generator_func.py.py
# @Author: ly
# @Date  : 2018/12/9


def g_func():
    print('I am starting')
    yield 1000
    print('after one yield')
    yield 1001


if __name__ == '__main__':
    d = g_func()
    """
    Output:
    I am starting
    1000
    after one yield
    1001
    """
    for i in d:
        print(i)
    print(next(d))
    print(next(d))

