#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : socket_chat.py
# @Author: ly
#. @Date  : 2018/12/2

import socket


def receive_msg(socket_ins):
    res_data, res_address = socket_ins.recvfrom(10<<10)
    print('your receive msg is %s, from %s' % (res_data.decode(), str(res_address)), end="\n")


def send_msg(socket_ins):
    to_ = input('send to ip: ')
    port_ = int(input('send to port: '))
    msg = input('msg:\n')
    # 为什么直接退了
    socket_ins.sendto(msg.encode(), (to_, port_))


if __name__ == '__main__':

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.12.117', 8888))

    while True:
        in_ = input('Please input your operation, 1 send message, 2 receive message, 3 exit')
        if in_ == '1':
            send_msg(udp_socket)
            pass
        if in_ == '2':
            receive_msg(udp_socket)
            pass
        if in_ == '3':
            break
            pass
        if in_ == '4':
            print('Wrong input')

    udp_socket.close()