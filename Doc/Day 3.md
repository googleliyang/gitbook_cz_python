# Day 3 Day: 10.24


## Yesterday

-  进制以及进制转换




- 变量

  - 1 - 2 变量, (堆栈内存无)， 可变不可变， 60分钟.... 例子生硬

- 数据类型  

  >  判断数据类型方法 type,  无需预定类型， 类型由值决定
  > isinstance(a, int)


  - Number（数字） int、float、bool、complex
    - python3 整数类型 int，表示为长整型，没有 python2 中的 Long

  - String（字符串）
  - Tuple（元组）
  - List（列表）
  - Set（集合）
  - Dictionary（字典）

>  其中不可变数据类型为 int string Tuple
  可变数据类型为 List Directory Set




## 运算符

- \+ - * / %

- \// : (向下取整) \** 多少次方

## 复合运算符


- 判断语句

## 内存

> 讲课 堆栈草草了事 运行内存 程序内存了结

- 运行内存
- 存储内存

python 中 变量的值存在于 栈内存


## Env


- python 3.6


- 变量定义


变量名称   =  值


## Python 3 与 Python2 区别



### Python 中 缩进要严格注意



## python 中的逻辑

 - not or and

## Tip


- Python 中不区分 '' ""
- 注释  #  ctrl + /s
- python 命令默认 2.x.x   python3 xx.py run by python3
- Python 定义变量不需要 定义 var
- Python 严格注意缩进
- attack = 20; Print('攻击力', attack)
- Python 换行是 4 空格
- 当不知道 赋值什么类型的 时候 赋值  None
- python 中  id() 查询 变量的存储空间
- 内严格 区分大小写 True, None
- 字符串和整数相互转换 int() str()
- 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
- Python可以同时为多个变量赋值，如a, b = 1, 2。
- Python 中以 is is not 来代替 ===
- 字符串可以和数字做乘法操作 repeat加法不可以
- Python 中 无 switch
- python 中缩进 建议是 4 个(但要保持一致)，不等于有警告
- 写代码时注意类型统一
- 2 << 2 == 2 ** 3   1 位是平方
- 多行字符串 ''' """
- 课补半天.


## Extension

- malloc func*

malloc()在内存中开辟动态地址空间，空间大小为（）内的整数。返回空间的首地址


## Class work

- calculate if the year is leap year

```

>>> [(month%12 + 3)//3 for month in range(1, 13)]
[1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]

```


## FAQ



- complex

> J（或J）表示-1的平方根（这是一个虚数）。 a是真正的数字部分，b是虚部(虚部而已后边加的是 -1 的平方根)。

![image-20181024153502711](/var/folders/lj/7gy8g4td0sl9tch9v2pft7n40000gn/T/abnerworks.Typora/image-20181024153502711.png)



- 不可变数据类型

  Python 中的不可变数据类型指的是 值变之后创建新的对象，内部采用引用计数来计算引用次数
  可变数据类型如字典等，append、+=等这种操作后，只是改变了变量的值不会创建新的对象，过
  对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址



- Python 堆栈

  > 二进制计算器 使用 二进制代替某些固定数值使用







