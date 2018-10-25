#! /usr/bin/env python3


def get_input(func, cons):

    while True:

        i = int(input(cons))

        if i == 0:
            exit('Bye, see you next time! ')

        func(i)


def cal_leap_year(i):

    c = i % 4 == 0 and i % 100 != 0 and 'is' or i % 400 == 0 and 'is' or 'is not'

    print(i, c, 'leap year')


def auto_call(num):

    if num == 1:
        print('Call father phone')


get_input(cal_leap_year, 'Please input year')
