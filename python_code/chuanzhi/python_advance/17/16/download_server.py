#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : download_server.py
# @Author: ly
# @Date  : 2018/12/3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('', 7777))

server_socket.listen(2 << 6)


while True:

    client_socket, address = server_socket.accept()
    print('接收到 来源 ip port %s' % str(address))

    data = client_socket.recv(2 << 9)

    file = open('../'+data.decode(), 'rb')

    res = file.read()

    client_socket.send(res)

    client_socket.close()

    file.close()


server_socket.close()


