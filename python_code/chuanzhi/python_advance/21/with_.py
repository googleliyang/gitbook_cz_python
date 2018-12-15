#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : with_.py
# @Author: ly
# @Date  : 2018/12/12


class MyTest:
    def __enter__(self):
        # return 返回值 为 with 后 as
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


with MyTest() as my:
    pass



