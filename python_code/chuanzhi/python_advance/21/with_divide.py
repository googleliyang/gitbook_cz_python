#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : with_divide.py
# @Author: ly
# @Date  : 2018/12/12


class Util:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __enter__(self):
        return self

    def div(self):
        return self.x/self.y

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("输入错误")
        return True


with Util(6, 0) as cal:
    res = cal.div()
    print(res)




