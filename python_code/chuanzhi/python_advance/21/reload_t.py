#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : reload_t.py
# @Author: ly
# @Date  : 2018/12/12

import A
import time


from imp import reload
# print(A.a)
while 1:
    reload(A)
    print(A.a)
    time.sleep(0.01)
