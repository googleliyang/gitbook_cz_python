#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : iter.py
# @Author: ly
# @Date  : 2018/12/9
from collections.abc import Iterable


class DataIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

    def __iter__(self):
        return self


class Data:
    def __init__(self):
        self.data = [1, 3, 7, 9, 8]

    def __iter__(self):
        return DataIterator(self.data)


if __name__ == '__main__':
    print('If Data is iterable %s' % isinstance(Data(), Iterable))
    d = iter(Data())
    # for i in Data():
    #     print(i)
    while True:
        try:
            i = next(d)
            print(i)
        except StopIteration as e:
            print('迭代完成')
            break
