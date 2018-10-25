def cal():
    f = input('Please input the first num')
    o = input('Please input the operation')
    s = input('Please input the second num')
    res = eval(f + o + s)
    print('the res is %d' % res)


def trans(a, b):
    [b, a] = [a, b]
    print('The a b val is a = %d, b=%d' % (a, b))


def check_weight(weight, height):
    return (height - 108) * 2 + 10 > weight > (height - 108) * 2 - 10


def cal_grade():

    t = 0

    for i in range(1, 6):
        t += get_input('输入学生成绩')

    print('The total score is %d' % t, 'The average is',   t / 5)


def get_input(msg):
    return int(input(msg))


cal_grade()


'''
cal()
trans(1, 2)
'''


