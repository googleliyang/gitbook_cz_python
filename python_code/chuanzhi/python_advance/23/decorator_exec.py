#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : decorator_exec.py
# @Author: ly
# @Date  : 2018/12/15

def setFunc(func):
    print('*'*10)
    def wrapper(*args, **kwargs):  # 接收不同的参数
        print('wrapper context')
        return func(*args, *kwargs)  # 再原样传回给被装饰的函数

    return wrapper


@setFunc
def show(name, age):
    print(name, age)


# show('tom', 12)
