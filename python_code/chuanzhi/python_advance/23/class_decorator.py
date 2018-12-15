#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : class_decorator.py
# @Author: ly
# @Date  : 2018/12/15


class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('my args is %s' % str(args))
        return print("I can be called")


@ Decorator
def cal(p1, p2):

    n = 0

    for i in range(10 << 10):
        n += i

cal(1, 2)
