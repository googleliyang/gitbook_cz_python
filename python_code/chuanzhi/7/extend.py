class Parent:
    def __init__(self, name):
        self.name = name

class Grand:
	def __init__(self, name):
		self.name = name
	def say(self):
		print('%s say..' %self.name)

class Child(Parent, Grand):
    pass


child = Child('qi')
child.say()
