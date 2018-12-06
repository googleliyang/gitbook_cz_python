import socket


def main():
    # 1 输入服务器ＩＰ　端口　文件名
    server_ip = input("服务器IP:")
    server_port = int(input("端口:"))
    file_name = input("请输入需要下载的文件名:")

    # 2 创建套接字   IPv4            基于字节流
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3 建立和服务器的连接　　(服务器ＩＰ　端口)
    tcp_socket.connect((server_ip, server_port))
    # 4 将文件名发送服务器
    tcp_socket.send(file_name.encode())

    # 5 一边接收数据　一边写入文件
    # 5.1 创建一个文件 用来保存数据
    file = open("下载_" + file_name, "wb")
    while True:
        # 5.2 接收
        file_data = tcp_socket.recv(4096)

        # 如果对端关闭连接 收b'' 意味着文件传输已经完成了
        if not file_data:
            print("文件下载完成了")
            break

        # 5.3 保存
        file.write(file_data)

    # 6 文件接收完成 关闭套接字/文件
    file.close()
    tcp_socket.close()

    
if __name__ == '__main__':
    main()
