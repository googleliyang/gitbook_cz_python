#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : udp.py
# @Author: ly
# @Date  : 2018/12/2

import socket

'''
 create socket

'''

broadcast_address = ('255.255.255.255', 6666)
# broadcast_address = ('192.168.12.255', 6666)

# remote_address = ('192.168.12.199', 8080)

upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

upd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

upd_socket.bind(('192.168.12.117', 7777))

while True:

    txt = input('Please input your message\n')

    upd_socket.sendto(txt.encode(), broadcast_address)

    print('----send done----')

    receive_data, remote_address = upd_socket.recvfrom(10<<10)

    print('receive data from %s data is %s' % (str(remote_address), receive_data.decode()))

upd_socket.close()
