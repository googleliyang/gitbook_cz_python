#! /usr/bin/env python3

const_msg = 'I am equal val'
f = 1.1
i = 1
e = 1
c = "a"
d = 1.1
fl = False


# v1 = input()
# v2 = input()

if __name__ == '__main__':
    # print(type(v1));
    # print('The total is', v1 + v2);
    # print('The a asc is', int(c));
    print(const_msg);
    print(type(f));
    print(type(i));
    print('The id of f is', id(f));
    print('The id of i is', id(i));
    print('The d int() convert is', int(d));
    print('instance of test type c is', isinstance(fl, bool));
    print('7.7 // 2 取整为', 7 // 2);
    print('2 的 三次方', 2 ** 3);
    print('e ++', e);
    print('e + c', e + d);

elif 2 > 1:

    print('Else if')

else:
    print('No condition data')


if not fl and d :
    print('I got out')

print('c or d res is', c or d)
print('false or d res is', False or d)
