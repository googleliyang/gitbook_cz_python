#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : encode.py
# @Author: ly
# @Date  : 2018/12/2

txt = input('Please input your message\n')

print(txt)

byts = txt.encode('UTF-8')

print('类型为 %s, 值为 %s' %(type(byts), byts))

print('转str后类型为 %s, 值为 %s' %(type(byts.decode('utf-8')), byts.decode()))




