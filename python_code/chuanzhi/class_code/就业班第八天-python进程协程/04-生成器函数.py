def gen():
    """不是普通函数  而是生成器函数含有yield关键字"""
    print("in gen")
    # 1 能够暂停当前代码的执行 然后把后面的值返回到 调用生成器代码的地方
    yield 1000
    # 2 当生成器代码继续执行的时候 紧接刚刚暂停的位置 继续往下执行
    yield 1001

    yield 1002


if __name__ == '__main__':
    # 生成器函数() 不再是执行代码  而是创建一个 生成器对象
    g = gen()

    # 生成器函数产生生成器对象 ---> 迭代器 next()
    i = next(g)
    print("接收到了生成器代码的值", i)
    i = next(g)
    print("接收到了生成器代码的值", i)

    for i in gen():
        print(i)