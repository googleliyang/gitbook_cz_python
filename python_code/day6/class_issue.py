#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : class_issue.py
# @Author: ly
# @Date  : 2018/10/29


_score_total, _total_score, _max_val, _min_val, _stu_num = 0, 0, 0, 0, 0


def _fun():
    _list = []
    global _stu_num
    global _max_val
    global _min_val
    global _score_total
    while True:
        try:
            i = input('Please input grade \n')
            i = int(i)
            if i < 0:
                print('no < zero, again')
                continue

            _max_val = _max_val > i and _max_val or i
            _min_val = _min_val < i and _min_val or i
            _stu_num += 1
            _score_total += i

        except ValueError:
            if i == 'over':
                break
            print('invalid input')

    return _list


res = _fun()
print('Total stu num is{}'.format(_stu_num))
print('Total score total is{}'.format(_score_total))
print('Min score max is{}'.format(_max_val))
print('Average score min is{}'.format(_min_val))
print('Average score average is{}'.format(_score_total / _stu_num))

