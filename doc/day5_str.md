

## print

```python

# \n 换行，\t 四个空格
print('a', end='')
print('b')


```

## python 提供的内置函数

- max() min() pow() 求幂 = ** abs() 求绝对值


- round // 四舍五入

- Math

 > import math
 
    - math.ceil() 向上取整
    - math.floor() 向下取整 
    - math.modf() 小数和整数分离
    
- String

    - \+ 拼接操作
    - 相乘操作k
    - [] 根据位置获取字符
    - len() 返回字符串长度
    - index({char}) 返回下标 从零开始
    - rindex({char}) 返回下标 从右边往左找 但是下标还是 从左往右
    - str2.index('o' 3) // 从下标 3 开始找
    - str2.index('o' 1, 4) // 从下标 1 - 4之间 开始找
    - find 找不到 -1 index 找不到报错 
    - count 查找出现的次数, 加参数区间 count('好', 1, 8)
    - str.replace('char', {newVal}) : return new string, old string can not be 
    
> 字符串切片

    - 转大写  str.upper()  str.lower()
    - 首字母大写 str.title() 
    - print(str4[2:]) // 从截取到最后
    - print(str4[:2]) // 0 - 2
    - print(str[:]) // 不变
    - print(str[2::3]) //2 位置开始 3 个字符走一下
    - print(str.swapcase()) // 大写转小写 小写转大写
    - str.capitalize() // 将整个字符串的首字母大写，其余小写
    - 字符串的拆分
        - str.split(' ') :return list 
        
    - str.join(Interable: interable) : return list
    
> 字符串判断
    
    - startwith('a', 1, 5) // 在 1 5  
    - endwith('b')
    - str.isXX
        - isupper() // 是佛全是大写小写
        - islower() 
        - isalpha() // 是否全都是字母   *
        - isdigit()  // 检测是否都是数字  *
        - istitle()  // 检测每个单词的首字母是否大写
        - isspace()  // 检测一个字符串是否全是空格  
        - isalnum()  // 检测是否是字符 'wwww安达市多1111，'.isalnum() ： false
        - lstrip()   // 去掉字符串左边的符号，默认是去除空格 *
        - rstrip()   // 去掉字符串右边的符号，默认是去除空格
        - strip()    // 去掉字符串两端的空格
        - ljsut() || rjust   // 往左边或右边默认用空格 补齐 参数里字符数量
        - str.center(40, '*') // 用 * 补齐 40位 将字符串放在中间 
        - str.zfill(40) // 用 0 补齐 40位 将字符串放在左边 
        
## ord() chr()

- ord 转 ASI 值， chr, 转 ASI 转为字母 
        
     
## Tip 

    - python 从右往左下标递减， 左到右递增
    - 程序通常前闭后开

## Faq

- sum([]) // param: 可 迭代..

    - [] 不属于数据类型?
    
- 字符串也属于 iterable

- 凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列。

- 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

- 可以被next()函数调用并不断返回下一个值的对象称之为迭代器（Iterator）！

```python

1.凡是可作用于for循环的对象都是Iterable
2.凡是可用用于next()函数的对象都是Iterator
3.iter()函数用于把Iterable容器，变成Iterator

```


- 内存地址问题

    得出字符串不可更改的结论

- Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。



