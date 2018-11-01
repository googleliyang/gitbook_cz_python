#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : day8.py
# @Author: ly
# @Date  : 2018/10/31

import random;


def single_list(l):
    for i in l:
        if l.count(i) > 1:
            l.remove(i)
            l[0] = ''
            # print(i, l.index(i))
    l.remove('')


def single_list2(l):
    return list(set(l))


_l = ['w', 'w', 'w', 'd', 'd', 'w', 'a']
# a_l = single_list2(_l)
# print(a_l)
# single_list(_l)

# print(_l)

lll = [1, 2]
lll.pop(2)

max((1,2,9), (8,1));


def _ran(x):
    for i, val in enumerate(x):
        _len = len(x) - 1
        _r = random.randint(i, _len)
        x[_r], x[i] = x[i], x[_r]
        print(_r)


_ran(_l)
print(_l)

