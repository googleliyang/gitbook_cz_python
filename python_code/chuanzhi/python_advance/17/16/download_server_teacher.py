import socket


# 1 创建TCP套接字 绑定　监听
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 7777))
server_socket.listen(128)

while True:
    # 2 接受连接
    client_socket, client_address= server_socket.accept()
    print("接受到了来自%s的连接请求" % str(client_address))

    # 3 接收文件名称
    file_name = client_socket.recv(4096).decode()

    # 4 根据文件名称　读取文件数据
    file = open(file_name, "rb")
    file_data = file.read() # 如果文件较大　可能存在问题

    # 5 使用ＴＣＰ套接字发送数据给客户端　关闭套接字
    client_socket.send(file_data)
    client_socket.close()
    file.close()

server_socket.close()
