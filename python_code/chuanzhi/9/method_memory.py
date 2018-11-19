class Dog:

	def say(self):

		print('wangwang')

dog1 = Dog()
dog2 = Dog()

print(dog1.say, dog2.say)
print(id(dog1.say), id(dog2.say))
