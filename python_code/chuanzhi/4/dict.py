#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : dict.py
# @Author: ly
# @Date  : 2018/11/10

dict_ = {'name': 'js', 'age': 10, 'use': 'web'}

for i in dict_:
    print(i)

print(dict_.values())
print(dict_.keys())
print(dict_.items())

for key, val in dict_.items():
    print('key %s, value %s' % (key, val))
