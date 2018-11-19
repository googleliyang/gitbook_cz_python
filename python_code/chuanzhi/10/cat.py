#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : cat.py
# @Author: ly
# @Date  : 2018/11/19


class Cat:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def say():
        print("123")


cat1 = Cat('cat 1')
cat1.say()

cat2 = Cat('cat2')
cat2.say()

