#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 多进程拷贝文件.py
# @Author: ly
# @Date  : 2018/12/8

import os
import multiprocessing


def copy_file(source_path, dest_path, file):
    r_f = open(source_path+'/'+file, 'rb')
    if os.path.isdir(dest_path):
        print('文件存在')
    else:
        print('文件不存在新创建')
        os.mkdir(dest_path)
    w_f = open(dest_path+'/'+file, 'wb')
    while True:
        read = r_f.read(2 << 9)
        w_f.write(read)
        if not read:
            break
    r_f.close()
    w_f.close()


def main():
    path = input("请输入要备份的目录")
    dirs = os.listdir(path)
    pool = multiprocessing.Pool(8)
    for item in dirs:
        print(path, item)
        # pool.apply_async(func=copy_file, args=(path, './copy_'+path, item))
        copy_file(path, './copy_'+path, item)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

