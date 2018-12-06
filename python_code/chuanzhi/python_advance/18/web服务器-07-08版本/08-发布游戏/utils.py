def make_response(status, response_body):
    """返回一个响应体200 OK  """
    # 状态行
    response_line = "HTTP/1.1 %s\r\n" % status
    # 响应头
    response_header = "Server: PWS/1.1\r\nContent-Type: text/html\r\n"
    # 空行
    blank_line = "\r\n"
    response_data = (response_line + response_header + blank_line).encode() + response_body
    return response_data