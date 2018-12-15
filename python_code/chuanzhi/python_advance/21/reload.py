#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : reload.py
# @Author: ly
# @Date  : 2018/12/12

import module1
import time
from imp import reload

while 1:
    reload(module1)
    print(module1.name)
    # time.sleep(0.5)
