import random


class Lover:
    def __init__(self, name):
        self.name = name
        # pick stack
        self.stack = Stack()

    def feeding(self, lover):
        # pick food by stack
        # call eat
        food = self.stack.pick_food()
        lover.eat(self, food)

    def eat(self, lover, food):
        print('{0} feed {1} eat {2}'.format(lover.name, self.name, food))


class Stack:
    def __init__(self):
        self.food = ['香蕉', '黄瓜', '茄子']

    def pick_food(self):
        i = random.randint(1, len(self.food) - 1)
        return self.food[i]


l_feed = Lover('刘亦菲')
l1 = Lover('me')

l_feed.feeding(l1)
l1.feeding(l_feed)
