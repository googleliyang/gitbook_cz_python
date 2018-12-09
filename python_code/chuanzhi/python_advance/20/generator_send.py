#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : generator_send.py
# @Author: ly
# @Date  : 2018/12/9


def my_gene():
    # print(123)
    number = yield 10
    print("i receive ", number)
    yield 20


if __name__ == '__main__':
    gen = my_gene()
    print(gen.send(None))
