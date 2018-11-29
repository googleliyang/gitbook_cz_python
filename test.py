#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: ly
# @Date  : 2018/11/23

import random


def get_ave(n, ran_int):
    list_ = []
    for i in range(0, n):
        # res = random.randint(1, 100)
        res = ran_int(1, 100)
        list_.append(res)

    list_.remove(max(list_))

    ave = sum(list_) / len(list_)

    return ave


ran_int = lambda start, end: random.randint(start, end)
res = get_ave(5, ran_int)
print(res)
