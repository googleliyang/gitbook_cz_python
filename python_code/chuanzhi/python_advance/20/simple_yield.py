#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : simple_yield.py
# @Author: ly
# @Date  : 2018/12/9


def work():
    print(123)
    yield 123
    print(456)


if __name__ == '__main__':
    d = work()
    print(next(d))
    print(next(d))
