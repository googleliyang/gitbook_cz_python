
## 列表

- 列表，容器，可存储不同类型数据, list， 
    
    - [{val1}, {val2}] 
    
     - List 方法
    
        - append 追加
    
     
- 列表属性和方法 

```python

_list = [] 
_list.append(12)
_list.extend([20, 30, 30])
_list.insert()
_list.insert()  # 参数为 [], return 为 [, []]



_list.remove() # 根据元素去删除
_list.clear()
_list.pop({position})
del _list(position)


_list.index({ele}) 
_list.index({ele}[, start, end])
_list.count({ele}) 


_list.reverse() # 反转输出 不会生成新列表 更改原列表


#  使用 内存地址  解释如下

_list.copy() # 赋值数据只拷贝一层
_list.deepcopy() # 可以拷贝多层

list6 = [1, 2, 3, ['a', 'b']]
list7 = list6
list7[0] = 5
list7[3][1] = 'ww'

# 6 [1, 2, 3, ['ww', 'b']]




```

## 元组 tuple
标志: ()
不可变，可存储任何类型的数据，可重复, 无添加删除等操作，查询即可

- 创建一个元素的元组

- t = (10, ) # 否则输出 int type((10)) -> output int

- 取值 tuple[index]


### 元组方法, 当不想被变时使用

- count({char})
- index({ele}, start, end) 

> 使用 len 方法长度

### 元组列表互转，list(), tuple()

## 字典 dict

- 常见一个空字典

- d1 = {}

- 字典无下标

- 字典键可以是  string 也可以是 int

- 键可变

### 常用方法

```python

setdefault() # 如果键存在则不变，如果不存在则修改 

dict[{key}] = value # 对字典某个值进行修

dict.update({dict}) # 一次添加多条数据 

dict.pop() # 删除元素

dict.get({index}) # 查询元素

dict[{index}] # 找不到报错 

dict.keys # 获取所有的键

dict.values # 获取所有的值

dict.items() # 获取键值对 

dict.get(name) == None


```

## 集合 {10, 20, 30}

> Set 无法取值，可便利

- 集合无下标, 不重复， 通常用来去重

- update 不可以参数为一个值

列表 元组 集合 字典 都可以往 集合里加 [], (), {}

- remove 根据元素去删除

> 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。


- pop 删除第一个, clear 全删

- discard 如果不存在不报错



# FAQ

- python 运行时 函数 变量 基本数据类型 引用数据类型内存中存储地址

- 使用 内存地址  解释如下

    _list.copy() # 赋值数据只拷贝一层
    
    _list.deepcopy() # 可以拷贝多层

- pass 站位 当 if: 后先不写 就先加个 pass

```python
if 2>1:
    pass
print(123)

```

## NextDay rem

- 列表特点 [1, ,2 ,3]

可变，有下标，可重复, 有序 q

> sort 排序会更改原列表

- 元组有下标，不可变

- deepcopy 引入包

```python

from copy import deepcopy

```

- set 无下标 pop 默认从左边开始删除 无序的


## 补充

> 字典如果用对象则 

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e

```

> Iterable & how to check obj if iterable

 An object capable of returning its members one at a time. 
 Examples of iterables include all sequence types (such as list, str, and tuple)
 and some non-sequence types like dict, file objects, and objects of any classes 
 you define with an __iter__() method or with a __getitem__() method that implements
 Sequence semantics. 


> 



