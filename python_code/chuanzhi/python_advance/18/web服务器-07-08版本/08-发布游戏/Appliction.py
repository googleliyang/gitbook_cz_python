import utils


def parse_http_request(http_request_data):
    """解析HTTP请求报文 返回一个字典"""
    """
    GET /index.html HTTP/1.1\r\n
    Host: 127.0.0.1:8080\r\n
    Connection: keep-alive\r\n
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36\r\n
    Accept-Encoding: gzip, deflate, sdch\r\n
    Accept-Language: zh-CN,zh;q=0.8\r\n
    \r\n"""
    # 1 按照\r\n切割
    data_lines = http_request_data.split("\r\n")
    # 2 获取到请求行中每一项数据
    data_list = data_lines[0].split(" ")

    # 3 创建一个字典 并且往其中添加键值对
    data_dict = dict()
    data_dict['METHOD'] = data_list[0]  # 方法
    data_dict['PATH_INFO'] = data_list[1]
    print(data_lines)
    # 4 把每个头都按照: 切割
    # Accept-Language: zh-CN,zh;q=0.8
    for header in data_lines[1:-2]:
        # ['Accept-Language','zh-CN,zh;q=0.8']
        headers = header.split(":")
        data_dict[headers[0]] = headers[1]

    return data_dict

def app(http_request_data, cur_game):
    """接收请求报文 处理结果 返回响应报文"""
    # 3.2 解析请求报文中第0行就是请求行
    # print(http_request_data)
    # 解析HTTP请求  获取到HTTP请求报文的字典
    di = parse_http_request(http_request_data)
    path_info = di['PATH_INFO']

    # 3.4 如果用户请求路径是/  表示首页
    if path_info == '/':
        path_info = '/index.html'
    print("获取到了用户的游戏请求%s" % cur_game)
    # 4 读取相应资源 打包成HTTP响应报文 发送给客户端
    # 4.1 读取资源          + /images/003.jpg
    try:
        # 尝试执行这里的代码
        file = open("./game/"+cur_game + path_info, "rb")
        html_data = file.read()
        file.close()
    except Exception as e:
        # 如果有异常  执行这里的代码
        file = open("./static/404.html", "rb")
        html_data = file.read()
        file.close()
        # http_response_data = ("HTTP/1.1 404 Not Found\r\n" + "Server: PWS/1.0\r\n" + "\r\n").encode() + html_data
        return utils.make_response('404 Not Found', html_data)
    else:
        # 如果没有异常执行这里的代码
        # 4.2 拼接响应报文     响应行                    头                      空行               响应体
        # http_response_data = ("HTTP/1.1 200 OK\r\n" + "Server: PWS/1.0\r\n" + "\r\n").encode() + html_data
        return utils.make_response('200 OK', html_data)

    finally:
        pass
