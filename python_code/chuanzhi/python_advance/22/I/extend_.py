#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : extend_.py
# @Author: ly
# @Date  : 2018/12/13


class Person:
    def __init__(self, action, name, age):
        self.action = action
        self.name = name
        self.age =age


class Child(Person):

    def __init__(self, id_card):
        self.id_card = id_card


xiao_ming = Child(12345678)
print(xiao_ming.age)
