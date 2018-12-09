
def myrange(max):
    cur = 0
    while cur < max:
        yield cur
        cur += 1
    # yield "hahah"   # 可以验证yield和return的区别
    return "hahah"
    print("---------")

if __name__ == '__main__':
    # for i in myrange(5):
    #     print(i)
    # 1 创建生成器对象
    mr = myrange(5)
    while True:
        try:
            # 2 获取生成器产生的下一个元素  print(next(mr))
            i = next(mr)
            print(i)
        except StopIteration as e:
            print("获取异常数据为%s" % e.value)
            break