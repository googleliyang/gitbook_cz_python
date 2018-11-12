_str = 'acdef'

for i in _str:
    if i is 'a':
        print('*', end='')
    elif i is 'b':
        break
    else:
        print(i, end='')
else:
    print('safe end')

b = ''' hello, "i'm li_lei"'''

c = "hi, 'i'm wang '"

d = "hi, \"i\'m ha\" "
print(b, c, d)

