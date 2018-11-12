#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : func.py
# @Author: ly
# @Date  : 2018/11/10


# 关键字参数
def print_(name, age):
    print('name is %s age is %s' % (name, age))


print_(age=13, name='js')

print(123)


# 默认参数
def print_default(name=1, *age):
    print(type(age))  # tuple
    print('name is %s age is %s' % (name, age))  # (10, 11, 12)


def print_dict(name=1, **age):
    print(name, age)


print_default(9, 10, 11, 12)
print_dict(a=1, b=2)


def cal_(a, *, c):
    print(a, c)


cal_(1, c=3)


size = 20


def con_():
    age = 1
    return lambda a, b: a + b + age + size


res = con_()(1, 2)
print(res)  # output 24

