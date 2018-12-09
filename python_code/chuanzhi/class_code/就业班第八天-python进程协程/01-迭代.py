from collections import Iterable
data = [1,2,3,4,5,6]
for i in range(5):
    print(i)

# 可迭代对象: 可以使用迭代器进行迭代访问的对象 常见都是容器类型
# 使用for循环遍历取值
# 1 判断对象是否是可迭代类型的 对象
# (对象, 类型)  判断对象是否是 类型 的
print(isinstance(1, int))
print(isinstance(1, str))
print(isinstance(data, Iterable))   # 判断对象是否是  可迭代Iterable类型的对象

class MyData(object):
    def __iter__(self):
        """返回 可迭代对象提供的迭代器 """
        pass

# 2 只有在类中实现了__iter__  类的对象才是可迭代类型的
md = MyData()
print(isinstance(md, Iterable))
for i in md:
    print(i)