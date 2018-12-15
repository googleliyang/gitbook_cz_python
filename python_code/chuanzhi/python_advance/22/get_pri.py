#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : get_pri.py
# @Author: ly
# @Date  : 2018/12/13


class My:
    def __init__(self, name):
        self.__name = name
        # print(self.__class__.mro())
        print(self.__dict__)


m = My(123)
print(m._My__name)
