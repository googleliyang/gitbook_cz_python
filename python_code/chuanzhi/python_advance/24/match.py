#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : match.py
# @Author: ly
# @Date  : 2018/12/16


import re

if __name__ == '__main__':
    res = re.match("hello", 'helloworld')
    print(res.group())
    print(res.span())
    print(res.start())
    print(res.end())

