''' 实现回调用'''

from p_02回调B import *

# 版本一 调用另外一个模块中的方法

# def func_a():
#     print('A-Show...')
#     # 调用func_b函数
#     func_b()
#
#
# if __name__ == '__main__':
#     func_a()
#     print('over')


# 版本二

from p_02回调B import *

def func_a():
    print('A_Show...')
    # 调用模块B中的func_b 函数，并将自己模块中的func_c传入进去
    func_b(func_c)

def func_c():
    print('C_show...')


if __name__ == '__main__':
    func_a()
    print('over')