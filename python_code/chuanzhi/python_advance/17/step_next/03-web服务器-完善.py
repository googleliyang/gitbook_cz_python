import  socket
"""
Web服务器= TCP服务器 + HTTP协议格式
01- 在用户请求网页的时候 总是返回一个固定的页面
02- 返回用户指定页面
03- 改进: 如果文件不存在 返回404错误
"""
if __name__ == '__main__':
    # 1 创建TCP 绑定 监听
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 地址重用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_socket.bind(('', 9999))
    tcp_socket.listen(128)

    # 2 接受来自 客户端/浏览器 连接
    while True:
        client_socket, client_addr = tcp_socket.accept()
        print("接受到来自%s的连接请求了" % str(client_addr))
        # 3 接收HTTP请求报文 解析数据获取用户的需求
        # 3.1 接收请求报文
        http_request_data = client_socket.recv(4096).decode()
        if not http_request_data:
            print("用户请求错误")
            continue

        # 3.2 解析请求报文中第0行就是请求行
        # print(http_request_data)
        request_line = http_request_data.split("\r\n")[0]

        # 3.3 从请求行中取出 资源请求路径 (切割请求行 获取第1个元素)
        path_info = request_line.split(" ")[1]
        print("获取到用户的请求路径 %s " % path_info)

        # 3.4 如果用户请求路径是/  表示首页
        if path_info == '/':
            path_info = '/index.html'

        # 4 读取相应资源 打包成HTTP响应报文 发送给客户端
        # 4.1 读取资源          + /images/003.jpg
        try:
            # 尝试执行这里的代码
            file = open("./static" + path_info, "rb")
            html_data = file.read()
            file.close()
        except Exception as e:
            # 如果有异常  执行这里的代码
            file = open("./static/404.html", "rb")
            html_data = file.read()
            file.close()
            http_response_data = ("HTTP/1.1 404 Not Found\r\n" + "Server: PWS/1.0\r\n" + "\r\n").encode() + html_data
        else:
            # 如果没有异常执行这里的代码
            # 4.2 拼接响应报文     响应行                    头                      空行               响应体
            http_response_data = ("HTTP/1.1 200 OK\r\n" + "Server: PWS/1.0\r\n" + "\r\n").encode() + html_data
        finally:
            # 不管有没有异常都会执行这里的代码
            # 4.3 发送
            client_socket.send(http_response_data)
            # 5 合适时间关闭连接 短连接实现
            client_socket.close()


    tcp_socket.close()