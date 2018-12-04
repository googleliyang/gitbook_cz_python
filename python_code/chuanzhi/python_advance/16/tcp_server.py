#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : tcp_server.py
# @Author: ly
# @Date  : 2018/12/3

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(('192.168.12.95', 8888))

tcp_socket.listen(2 << 6)

client_socket, address = tcp_socket.accept()

# 持续监听
while True:

    data = client_socket.recv(10 << 10)

    if not data:
        print('用户断开连接')
        break

    print('get data from client is %s' % data.decode())

    client_socket.send(data)


client_socket.close()
tcp_socket.close()
