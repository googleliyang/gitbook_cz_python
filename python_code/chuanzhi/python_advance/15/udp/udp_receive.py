#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : udp_receive.py
# @Author: ly
# @Date  : 2018/12/2

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : udp.py
# @Author: ly
# @Date  : 2018/12/2

import socket

'''
 create socket

'''


upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

upd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

upd_socket.bind(('', 6666))


receive_data, remote_address = upd_socket.recvfrom(10<<10)

print('receive data from %s data is %s' % (str(remote_address), receive_data.decode()))

upd_socket.close()

