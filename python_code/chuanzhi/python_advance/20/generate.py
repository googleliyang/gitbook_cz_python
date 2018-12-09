#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : generate.py
# @Author: ly
# @Date  : 2018/12/9


def main():
    x = [x for x in range(10)]
    print('x 长度为 %s, x 为' % (len(x)), x)
    y = (y for y in range(10))
    print(type(y))
    for i in y:
        print(i)


if __name__ == '__main__':
    main()
    pass
