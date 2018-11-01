

## 将 iterable 与 iterator 用处 以及  tuple 参数

```python
Python中iterable被认为是一个对象，
这个对象可以一次返回它的一个成员（也就是对象里面的元素），由此可知，
Python中的string，list，tuple，dict，file，xrange都是可迭代的，
都属于iterable对象，可迭代的对象都是可以遍历的，实际上Python中有很多iterable类型是使用iter()函数来生成的。

```

- 判断是否可以迭代

```python

from collections import Iterable

isinstance({}, Iterable) # True 

from collections import Iterator

isinstance((), Iterator) # False 


```

## 函数, 封装

代码重复时使用


## FAQ

- list 属于 iterable， 继承关系在哪体现的 ?

```python

# 继承关系 ？
Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，
或者定义了可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中全面解释)，
那么它就是一个可迭代对象。

```

```python
# 源码未实现
 def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

```

```python
# 如下源码体现在何处 

entry/slot ->关联容器（键）

一个entry的定义如下：

typedef struct {  

Py_ssize_t me_hash;  //记录me_key 的散列值，避免每次都要计算

PyObject *me_key;   //指向键

PyObject *me_value; //指向值

} PyDictEntry;

'''
因为key和value 都是PyObject，故什么东西都可以放进去Dict
entry有三种状态：
①Unused态 →key，value = Null
②Active 态 → key！= dummy，key！=Null，value ！= Null
③Dummy 态 → key = Dummy， value = Null
三态的转换关系如下：
--------------------- 
'''

```

- iterable 与 iterator

```python
可迭代的 与 迭代器对象 

个包含与被包含的关系，如果一个对象是迭代器，那么这个对象肯定是可迭代的；但是反过来，如果一个对象是可迭代的，那么这个对象不一定是迭代器。

```
