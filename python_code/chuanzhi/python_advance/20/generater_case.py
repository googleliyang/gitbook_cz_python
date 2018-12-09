#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : generater_case.py
# @Author: ly
# @Date  : 2018/12/9


def my_range(max):
    i = 0
    while i < max:
        yield i
        i += 1
    return 123


if __name__ == '__main__':
    # for i in my_range(5):
    #    print(i)
    d = my_range(5)
    while True:
        try:
            print(next(d))
        except StopIteration as e:
            print(e)
            break

