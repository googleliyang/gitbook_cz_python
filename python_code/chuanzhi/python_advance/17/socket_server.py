import socket


"""
在用户请求网页的时候 总是返回一个固定的页面
"""
if __name__ == '__main__':
    # 1 创建TCP 绑定 监听
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_socket.bind(('', 9999))
    tcp_socket.listen(128)

    # 2 接受来自 客户端/浏览器 连接
    while True:
        client_socket, client_addr = tcp_socket.accept()
        print("接受到来自%s的连接请求了" % str(client_addr))
        # 3 接收HTTP请求报文 解析数据获取用户的需求 - 暂时不用
        client_socket.recv(4096)
        # 4 读取相应资源 打包成HTTP响应报文 发送给客户端
        # 4.1 读取资源
        file = open("./index.html", "rb")
        html_data = file.read()
        # 4.2 拼接响应报文响应行头空行响应体
        http_response_data = ("HTTP/1.1 200 OK\r\n" + "Server: PWS/1.0\r\n" + "\r\n").encode() + html_data

        # 4.3 发送
        client_socket.send(http_response_data)

        # 5 合适时间关闭连接 短连接实现
        client_socket.close()
        file.close()

    tcp_socket.close()
