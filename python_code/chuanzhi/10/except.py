def func1():
    open('a.txt')
    print('after except')


if __name__ == "__main__":
    try:
        func1()
    except Exception:
        print('Get a except')
    print('continue run')
