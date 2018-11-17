class Person:
	def __init__(self, age):
		if age > 10:
			self.__age = 20
		else: 
			self.__age = 5

	def set(self, age):
		self.__age = age

	def get(self):
		return self.__age


person = Person(12)
print(person.get())

