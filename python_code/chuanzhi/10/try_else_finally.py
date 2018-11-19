def func01():
    return open('a.txt')


def test():
    f = None
    try:
        f = func01()
    except Exception as e:
        print('异常信息为 =', e)
    else:
        print('没有异常')
    finally:
        # 有异常 f 无值你怎么关
        f.close()
        print('有无异常均走')


if __name__ == '__main__':
    test()
