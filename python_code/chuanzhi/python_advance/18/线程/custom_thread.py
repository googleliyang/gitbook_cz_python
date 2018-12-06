#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : custom_thread.py
# @Author: ly
# @Date  : 2018/12/6

import threading
import time


a = 0


class MyThread(threading.Thread):

    def __init__(self, lock):
        super().__init__()
        self.lock = lock

    def run(self):
        self.say()
        global a
        for i in range(1000000):
            # print('Thread name', threading.current_thread().name)
            # time.sleep(1)
            self.lock.acquire()
            a += 1
            self.lock.release()
        pass

    def say(self):
        print('I say...')


if __name__ == '__main__':
    lock = threading.Lock()
    mt = MyThread(lock)
    mt1 = MyThread(lock)
    mt.start()
    mt1.start()
    mt.join()
    print('after child thread num is', a)



