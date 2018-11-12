#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : extract_param.py
# @Author: ly
# @Date  : 2018/11/12


def call_(*args, **kwargs):
    print(args)
    print(kwargs)


def call1_(*args, **kwargs):
    call_(*args, **kwargs)


call1_(1, 2, 3, name='zs')
