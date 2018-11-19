def func01():
	# r = 1 / 0
	open('a.txt')

def test():
	try:
		func01()
	except ZeroDivisionError as result:
		print(result)

def test1():
	try:
		func01()
	except ZeroDivisionError  as result:
		print(result)

if __name__ == '__main__':
	test1()
	print('done...')

