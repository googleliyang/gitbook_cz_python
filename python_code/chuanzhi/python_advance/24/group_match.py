#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : group_match.py
# @Author: ly
# @Date  : 2018/12/16


import re


if __name__ == '__main__':
    res = re.search("asd", 'asdefasd')
    print(res.group())# output asd 只匹配到了 第一个 asd
