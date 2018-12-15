#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : c3.py.py
# @Author: ly
# @Date  : 2018/12/13


class Parent:
    def __init__(self, name):
        self.name = 'people'

    def say(self):
        print('wuwu')


class ChildA(Parent):
    pass


class ChildB(Parent):
    def say(self):
        print('B wuwuw')


class C(ChildA, ChildB):
    pass


c = C('')
c.say()
