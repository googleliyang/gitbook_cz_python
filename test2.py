#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: ly
# @Date  : 2018/11/23

import random


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):

        return '{0}, 年龄{1}, 成绩{2}, {3}'.format(self.name, self.age, self.grade, self.grade < 60 and '成绩不合格' or '及格')


if __name__ == '__main__':
    grade = lambda s, e: random.randint(s, e)
    s1 = Student('zhangsan', 23, grade(0, 100))
    s2 = Student('lisi', 19, grade(0, 100))
    s3 = Student('wangwu', 30, grade(0, 100))
    list_= [s1, s2, s3]
    fs = open('b.txt', 'w')
    for i in list_:
        fs.write(str(i) + '\n')

    fs.close()

