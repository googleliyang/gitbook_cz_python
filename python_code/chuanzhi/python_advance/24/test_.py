#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_.py
# @Author: ly
# @Date  : 2018/12/15

import re

res = re.search('\\\\', '\\')
print(res.group())
