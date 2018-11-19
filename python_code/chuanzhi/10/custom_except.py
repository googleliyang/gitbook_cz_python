class MyError(Exception):
	def __str__(self):
		return '请输入一个数字'


age = input('Please input your age')

def checkAge():
	try:
		if (int(age) > 20):
			raise MyError()
	except Exception as e:
		print('异常为 = ', e)

checkAge()

