#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : download_file.py
# @Author: ly
# @Date  : 2018/12/3

import socket

ip = input('Ip:')
port = int(input('Port:'))
file_name = input('file_name:')

tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_s.connect((ip, port))

tcp_s.send(file_name.encode())

file = open('download' + file_name + '.png', 'wb')

while True:
    res = tcp_s.recv(2 << 9)
    file.write(res)
    if not res:
        print('download finish')
        break


tcp_s.close()
file.close()





