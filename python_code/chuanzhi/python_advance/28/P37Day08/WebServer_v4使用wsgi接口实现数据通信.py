
# 面向对象修改数据
import socket
import re
import multiprocessing

# 导入模块
import WebFrame_v4 as WebFrame


class WEBServer(object):
    #在初始化方法中完成服务器Socket对象的创建
    def __init__(self):
        """用来完成整体的控制"""
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 用来重新启用占用的端口
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定IP和端口号
        self.tcp_server_socket.bind(("", 7890))

        # 3. 设置套接字监听连接数(最大连接数)
        self.tcp_server_socket.listen(128)


    def service_client(self,new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求相关信息
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        #将请求头信息进行按行分解存到列表中
        request_lines = request.splitlines()
        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        #正则:  [^/]+ 不以/开头的至少一个字符 匹配到/之前
        #      (/[^ ]*) 以分组来匹配第一个字符是/,然后不以空格开始的0到多个字符,也就是空格之前
        #      最后通过匹配可以拿到 请求的路径名  比如:index.html
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        #如果匹配结果 不为none,说明请求地址正确
        if ret:
            #利用分组得到请求地址的文件名,正则的分组从索引1开始
            file_name = ret.group(1)
            print('FileName:  ' + file_name)
            #如果请求地址为 / 将文件名设置为index.html,也就是默认访问首页
            if file_name == "/":
                file_name = "/index.html"

        # 根据提取出来的请求地址，判断是请求页面是动态还是静态
        if file_name.endswith('.py'):
            # 判断成功，表示是动态


            # 通过模块名，调用访问，得到响应数据
            # 准备一个字典，将服务器解析出来的客户端请的地址存到字典里

            # application 提供了一个服务器和应用程序之间的通信接口
            # 服务器只需要调用这个接口就可以，不需要去考虑谁实现这个接口方法
            # 应用程序只需去实现这个接口，不需要去考虑谁来调用这个接口

            env = {'PATH_INFO': file_name}
            body = WebFrame.application(env, self.start_response)



            # 准备好响应行和响应头
            # 响应行
            line = 'HTTP/1.1 %s\r\n' % self.__status
            # 响应头
            header = 'Server: MiniWeb 1.0\r\n'

            # 拼接保存回来的响应头数据
            for t in self.__params:
                # t 里获取的就是一个列表中的元组，保存是响应头的key和 value
                header += '%s: %s\r\n' % t

            # 拼接响应报文
            data = line + header + '\r\n' + body
            # 通过客户端连接将响应报文发送回去
            new_socket.send(data.encode())


        else:
            # 2. 返回http格式的数据，给浏览器
            try:
                #拼接路径,在当前的html目录下找访问的路径对应的文件进行读取
                f = open("./html" + file_name, "rb")
            except:
                #如果没找到,拼接响应信息并返回信息
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                #如果找到对应文件就读取并返回内容
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                #如果想在响应体中直接发送文件内的信息,那么在上面读取文件时就不能用rb模式,只能使用r模式,所以下面将响应头和响应体分开发送
                #response += html_content
                # 2.2 准备发送给浏览器的数据
                # 将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response body发送给浏览器
                new_socket.send(html_content)

        # 关闭套接
        new_socket.close()

    # 定义一个用来实现回调的函数
    # 这个函数有两个参数，1.用来保存状态信息，2，用来保存响应头信息
    def start_response(self,status, params):
        # 这个函数只用来实现保存信息
        self.__status = status
        self.__params = params


    def run(self):
        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            #因为新线程在创建过程中会完全复制父线程的运行环境,所以父线程中关闭的只是自己环境中的套接字对象
            #而新线程中因为被复制的环境中是独立存在的,所以不会受到影响
            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()

def main():
    webServer = WEBServer()
    webServer.run()

if __name__ == "__main__":
    main()