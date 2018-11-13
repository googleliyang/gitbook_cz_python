def read():
        # 如果文件很大会直接崩溃哦, 所以读文件时，建议一次  读 1M / 1 行 1024, while true 读写
    f = open('./test.txt', 'r')
    cont = f.read()
    print(cont)
    cont = f.read()
    print(cont)
    cont = f.read()
    print(cont == None)
    cont = f.read()
    # 注意 文件读完之后，每次read 都会返回一个 可被 repr 成的 '', 文件读完之后会成为 ''
    print(repr(cont))
    f.close()


def write():
    f = open('./test.txt', 'w')
    f.write('''I'm the data after update''')
    f.close()


def append():
    f = open('./test.txt', 'a')
    f.write(''' I'm append data''')
    f.close


def read_img():
    f = open('../../../imgs/4/debug.png', 'rb')
    cont = f.read()
    print(cont)


# write()
# append()
# read()
read_img()
