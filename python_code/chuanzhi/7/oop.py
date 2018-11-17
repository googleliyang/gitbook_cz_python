class Tem:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name is {}'.format(self.name)

    def __del__(self):
        print('{} is deleted'.format(self.name))


tem = Tem('li', 18)
# tem2 = Tem('lii', 18)
tem3 = tem4 = tem
print('del tem before')
del tem
