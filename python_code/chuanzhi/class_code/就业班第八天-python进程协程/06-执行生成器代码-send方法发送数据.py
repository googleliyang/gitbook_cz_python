

def myrange(max):
    cur = 0
    while cur < max:
        number = yield cur
        print("接收到了来自外界的数据 %s" % number)
        cur += 1

# 1 创建生成器对象
mr = myrange(5)
i = mr.send(None)
print("11111", i)
# i = next(mr)
# print("22222", i)
i = mr.send('1001')
print('33333',i)