class parent:
	def __init__(self):
		self.name = 'wang'
	def say(self):
		print('yeah, I say')



class child(parent):
	def __init__(self):
		pass

# pythond 的继承 不强制构造函数调用父类
c = child()
c.say()
