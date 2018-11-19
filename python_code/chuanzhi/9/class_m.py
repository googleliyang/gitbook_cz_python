class Dog:
    type = 1

    def update(self):
        self.type = 2

    @classmethod
    def show(self):
        self.type = 2


dog = Dog()
print(dog.type)
# dog.show() # 122
dog.update() # 121
print(dog.type)
print(Dog.type)
