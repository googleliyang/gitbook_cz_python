class Test(object):
    def __init__(self):
        self.__name = 'li'
        self.age = 24

    def print_(self):
        print('name is %s' % self.__name)


class modal(Test):
    def call(self):
        print('age is %s' % self.age)
        # print('name is %s' % self.name)


m = modal()
m.call()
m.print_()
