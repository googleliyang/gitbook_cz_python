#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : process.py
# @Author: ly
# @Date  : 2018/12/8


import multiprocessing
import os
import time


def c_process_func(name, play):
    while True:
        print('我是子进程, 我叫 %s 我演过 %s 我的 pid 是 %s' % (name, play, multiprocessing.current_process().pid))
        print('我是子进程，我的父id 是 %s' % os.getppid())
        time.sleep(1)


def main():
    """单进程 单线程 之前写的代码在主线程上"""
    # c_p = multiprocessing.Process(target=c_process_func, args=('zhaobenshan',), kwargs={'play':'xiaopin'})
    # c_p.start()
    # 最好设置大小不然内存无限大，就容易吃崩了
    q = multiprocessing.Queue(3)
    q.put(1)
    q.put(2)
    q.put(3)
    print('判断队列是否为空 %s ' % q.empty())
    print('判断队列是否为满了 %s ' % q.full())
    # Raises NotImplementedError on Mac OSX because of broken sem_getvalue()
    # print('队列大小 %s' % q.qsize())
    print('第一1次取值', q.get())
    print('第二次取值', q.get())
    print('第三次取值', q.get())


if __name__ == '__main__':
    main()
