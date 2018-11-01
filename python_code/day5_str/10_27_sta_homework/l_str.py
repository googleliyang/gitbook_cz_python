# Number 1
def num_get(start, end, division_num=5):
    _res = []
    while start <= end:
        if start % 3 is 0:
            _res.append(start)
            _p = len(_res) % division_num
            print(str(start) + '  ', end=_p is 0 and '\n' or '')
        start += 1
    return _res


# Number 2
def login():
    name, password = 'admin', '111'
    for i in range(3):
        _name = input('Please input username')
        _pass = input('Please input password')
        if _name == name and _pass == password:
            print('Login success')
        else:
            if i < 3:
                print('Login error, You still have %d times' % (2 - i))


# Number 3
class Bank:

    __name = 'admin'
    __pass = '111'
    __credit = 100
    __login_time = 3

    @staticmethod
    def _welcome():
        print('Welcome!')

    def go_login(self):
        __name = input('username:')
        __pass = input('pass:')
        self.login(__name, __pass)

    def ___ope_welcome(self):
        _ope = input('hi, %s Choose a selector, 1 query, 2 deposit, 3 __withdraw, 4 return!' % self.__name)
        _ope = int(_ope)
        if _ope == 1:
            print('Your balance is %s' % self.__credit)
        elif _ope == 2:
            _mon = input('Please input how much you will deposit')
            self.__top(_mon)
        elif _ope == 3:
            _mon = input('Please input how much you will __withdraw')
            self.__withdraw(_mon)
        elif _ope == 4:
            exit('See you next time')
        else:
            print('operate wrong')
            
        self.___ope_welcome()

    def login(self, n, p):
        if n == self.__name and p == self.__pass:
            self.___ope_welcome()
        else:
            self.__login_time -= 1
            print('login error, you have %d time' % self.__login_time)
            if self.__login_time > 0:
                self.go_login()

    def __top(self, money):
        money = Bank.validate(money)
        self.__credit += money

    def __withdraw(self, money):
        money = Bank.validate(money)
        self.__credit -= money

    @staticmethod
    def validate(money):
        if type(money) != int:
            money = int(money)
        return money


# Number 4
def get_num(start, end, step=2):
    _sum, _time = 0, 0
    while start <= end:
        if _time % 2 is 0:
            _sum += start
        else:
            _sum -= start
        _time += 1
        start += step
    return _sum


def get_num2(start, end, step):
    _times = end // step
    even = _times % 2 is 0
    return even and start or 0 + (_times//2+1)*step*(even and 1 or -1)


# Number 5
# 逻辑: 公共为一对兔子逻辑，之后每生成一对兔子，递归一次，月份(总月份 - 出生月, 操作 函数外 total_num 变量
def get_rabbit_num(init_rabbit_num, end_month, pregnancy_month):

    total_num = init_rabbit_num

    def _get_num(mon):
        nonlocal total_num
        # if pregnancy_month = 0, small than pregnancy_month - 1, same res
        for i in range(1, mon):
            # - 1 such as start from 0
            if i >= pregnancy_month - 1:
                _get_num(mon - i)
                total_num += 1

    for j in range(init_rabbit_num):
        _get_num(end_month)

    return total_num


# 斐波那契数列(数学规律 后数值为前两个数之和)
def cal_rabbit_num(m):
    if m is 1 or m is 2:
        return 1
    else:
        return cal_rabbit_num(m - 1) + cal_rabbit_num(m - 2)


# 兔子方式 3
def cal_r(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b

