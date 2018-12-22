'''
    函数嵌套调用
'''

# 函数嵌套调用
def func_a():
    print('A-Show ...')
    func_b()


def func_b():
    print('B-Show ...')
    func_c()


def func_c():
    print('C-Show ...')


if __name__ == '__main__':
    func_a()