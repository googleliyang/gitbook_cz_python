total = 0  # 这是一个全局变量


# 可写函数说明
def get_sum(arg1, arg2):
    # 返回2个参数的和."
    global total
    print('global total is %d' % total)
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


get_sum(1, 3)
