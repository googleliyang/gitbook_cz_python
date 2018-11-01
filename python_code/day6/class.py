#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : class.py
# @Author: ly
# @Date  : 2018/10/29


def _fun():

    _list = []
    while True:
        try:
            i = input('Please input grade \n')
            i = int(i)
            if i < 0:
                print('no < zero, again')
                continue
            _list.append(int(i))
        except ValueError:
            if i is 'over':
                break
            print('invalid input')

    return _list


res = _fun()
print('Total stu num is{}'.format(len(res)))
print('Total score num is{}'.format(sum(res)))
print('Max score num is{}'.format(max(res)))
print('Min score num is{}'.format(min(res)))
print('Average score num is{}'.format(sum(res) / len(res)))


