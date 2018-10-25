#! /usr/bin/env python3


def cal_num(i, v):
    if i % v == 0:
        return i
    else:
        return 0


def even_odd():

    odd_sum = even_sum = 1
    for i in range(1, 101):
        print(i)
        odd_sum += cal_num(i, 3)
        even_sum += cal_num(i, 2)

    print('The total of odd sum is %d, even_sum is %d' % (odd_sum, even_sum))
    
    
def cal_num(start_num, end_num):
    total = 0
    while start_num <= end_num:
        total += start_num
        start_num += 1
    
    return total    
     
        
def get_num(border_num, num):

    total = i = 0
    while i <= border_num:
        if i % num == 0:
            total += i

    return total


even_odd()

