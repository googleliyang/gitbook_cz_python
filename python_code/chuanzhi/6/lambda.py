

def cal(a, b, command):
    return command(a, b)


res = cal(1, 2, lambda a, b: a + b)
print(res)
