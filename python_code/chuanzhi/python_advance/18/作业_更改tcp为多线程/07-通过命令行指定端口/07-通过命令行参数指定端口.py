import sys
import socket
import threading
import Appliction


"""
Web服务器= TCP服务器 + HTTP协议格式
01- 在用户请求网页的时候 总是返回一个固定的页面
02- 返回用户指定页面
03- 改进: 如果文件不存在 返回404错误
面向过程  一个函数-功能
面向对象  一个类  -角色 带功能  把属性和操作属性的方法封装在一个类中
"""


class HTTPServer(object):
    """为用户提供web服务"""
    def __init__(self, port):
        """初始化对象的属性"""
        # 1 创建TCP 绑定 监听
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 地址重用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', port))
        server_socket.listen(128)

        # 保存一个套接字对象的引用
        self.server_socket = server_socket

    def start(self):
        """启动web服务"""
        # 2 接受来自 客户端/浏览器 连接
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("接受到来自%s的连接请求了" % str(client_addr))
            # 调用专门用来处理客户端请求的方法
            th = threading.Thread(target=self.client_request_handler, args=(client_socket,))
            th.start()
            # self.client_request_handler(client_socket)

    def client_request_handler(self,client_socket):
        """专门用来处理每个客户端的HTTP请求"""
        # 3 接收HTTP请求报文 解析数据获取用户的需求
        # 3.1 接收请求报文
        http_request_data = client_socket.recv(4096).decode()
        # 如果客户端已经断开连接了 收数据是b'' 就没有必要继续往下执行了
        if not http_request_data:
            print("用户请求错误")
            return

        # 调用模块的方法 处理HTTP请求报文 返回值就是响应报文
        http_response_data = Appliction.app(http_request_data)

        # 不管有没有异常都会执行这里的代码
        # 4.3 发送
        client_socket.send(http_response_data)
        # 5 合适时间关闭连接 短连接实现
        client_socket.close()
if __name__ == '__main__':
    # print(sys.argv)
    # 判断参数个数必须要大于等于2个  并且 全是由数字构成的
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        # 列表中每个元素都是字符串类型
        port = int(sys.argv[1])

        # 创建一个web服务
        http_server = HTTPServer(port)
        # 启动服务
        http_server.start()
    else:
        print("参数用法错误 python3 web.py 8080")
        # 降低了 参数和 代码的耦合度;以后修改参数就不用对代码做任何的修改了