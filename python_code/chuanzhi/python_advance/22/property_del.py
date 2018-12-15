#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : property_.py
# @Author: ly
# @Date  : 2018/12/13


class Person:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def del_x(self):
        del self.__name

    name = property(get_name, set_name, del_x, 'hello')


if __name__ == '__main__':
    person = Person('zs', 100)
    person.name = 'x12s'
    print(person.get_name())
    # del person.name
    # print(person.name)
    print(person.get_name.__doc__)

