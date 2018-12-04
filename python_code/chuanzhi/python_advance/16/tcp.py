import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = ('192.168.12.95', 8888)

    tcp_socket.connect(address)

    tcp_socket.send(('hello miss!').encode())

    # 阻塞 收不到数据不会往下执行
    receive_data = tcp_socket.recv(10 << 10)

    if receive_data:
        print('收到的数据 %s' % receive_data.decode())
    else:
        # receive_data = b''
        print('对方断开了连接')

    tcp_socket.close()


if __name__ == '__main__':
    main()
