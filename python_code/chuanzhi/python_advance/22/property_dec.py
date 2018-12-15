#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : property_.py
# @Author: ly
# @Date  : 2018/12/13


class Person:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    def get_name(self):
        return self.__name

    @property
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    # name = property(fset=set_name)
    # name = property(get_name, set_name)


if __name__ == '__main__':
    person = Person('zs', 100)
    person.name = 'x12s'
    # print(person.get_name())
    print(person.name)
    print(person.get_name())
    del person.name
    print(person.get_name())

