#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : mul_return.py
# @Author: ly
# @Date  : 2018/11/12


def call_():
    return 10, 20, 30


a, b, c = call_()
print(a, b, c)


def call1_(name, age=10, *args, **dict_):
    print(age, args[1], dict_)


call1_(5, 20, 1, 2, a=1)


a = 2900
b = 2900
print(id(a), id(b))
