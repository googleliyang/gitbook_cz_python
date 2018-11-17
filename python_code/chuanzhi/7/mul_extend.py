class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class Prentice(Master):
    def __init__(self):
        print('我被调用了')
        self.kongfu = "猫氏煎饼果子配方"
        self.money = 10000  # 亿美金

    def make_cake(self):
        self.__init__()  # 执行本类的__init__方法，做属性初始化 self.kongfu = "猫氏...."
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    # 调用父类方法格式：父类类名.父类方法(self)
    def make_old_cake(self):
        Master.__init__(self)  # 调用了父类Master的__init__方法 self.kongfu = "古法...."
        Master.make_cake(self)  # 调用了父类Master的实例方法


class PrenticePrentice(Prentice):  # 多层继承
    pass


pp = PrenticePrentice()
pp.make_cake()  # 调用父类的实例方法
pp.make_old_cake()

print(pp.money)
