#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Thread.py
# @Author: ly
# @Date  : 2018/12/6


import threading
import time


def sing(singer, song):
    for i in range(3):
        print('singer %s , %s' %(singer, song))
        time.sleep(1)


def dance(dancer, name):
    print('线程名称', threading.current_thread().name)
    for i in range(3):
        print('存活线程', threading.enumerate())
        print('singer %s , %s' %(dancer, name))
        time.sleep(1)


def main():
    for i in range(3):
        print('What do you do ?')
        time.sleep(1)


if __name__ == '__main__':
    # s_th = threading.Thread(target=sing, args=('韩红',), kwargs={'song': '那片海'})
    d_th = threading.Thread(target=dance, args=('周杰伦',), kwargs={'name': 'let it go'}, name='dance thread', daemon=True)
    # s_th.start()
    d_th.start()
    # print('存活线程', threading.enumerate())
    # main()
    # s_th.join()
    # d_th.join()
    # print('join后存活线程', threading.enumerate())
    # print('----I have got it----')
