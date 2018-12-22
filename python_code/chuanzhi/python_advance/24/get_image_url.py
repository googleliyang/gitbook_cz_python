#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : get_image_url.py
# @Author: ly
# @Date  : 2018/12/15

import re

add = """<img data-original="http://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131918_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">"""


def get_src():
    # res = re.search("src=(.*\.jpg|png)", add)
    # $ 表示一行结尾自然匹配不出！
    res = re.search(r"src=(.*)>$", add)
    if res:
        print(res.group())
    else:
        print('未找到您要匹配的字符串')


def get_src1():
    # ? 表示尽可能少的匹配 * 这里至少可以匹配到最近的 一个 "
    return re.search('.*src="(.*?)"', add)


if __name__ == '__main__':
    # get_src()
    # res = get_src1()
    # print(res.group(1))
    str_ = 'c:\\\\ww\\aa'
    res = re.match('c:\\\\\\\\ww\\\\aa', str_)
    print(res.group())
    # output c:\\ww\aa


