
# 封装一个函数,函数有一个参数，用来接收服务器传递 过来的客户请求址


def app(file_name):

    # 判断具体是哪个页面
    if file_name == '/index.py':
        # 访问的是首页

        # 响应体
        body = '<h1>Index Page Run v3</h1>'
    elif file_name == '/center.py':
        # 访问的是个人中心页面

        # 响应体
        body = '<h1>Center Page Run v3</h1>'

    else:
        # 访问的是任意页面

        # 响应体
        body = '<h1>Other Page Run v3</h1>'

    # 将数据返回
    return body