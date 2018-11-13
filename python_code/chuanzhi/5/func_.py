#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : func_.py
# @Author: ly
# @Date  : 2018/11/12

a = 10


# never use sum_
def update(sum_):
    sum_ = 0
    print(sum_)  # 0


update(a)
print(a)  # 10

