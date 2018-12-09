from collections import Iterable, Iterator

class MyDataIter(object):
    """访问 可迭代类型MyData 的对象的数据   为用户简介访问可迭代对象中每一个数据"""
    def __init__(self,data):
        self.data = data
        self.index = 0   # 记录位置下标
    def __next__(self):
        """为用户提供下一个元素的值 位置自动往后+1"""
        # 如果下标已经大于等于 元素的个数  抛出停止迭代StopIteration
        if self.index >= len(self.data):
            raise StopIteration
        else:
            # 返回用户需要的下一个元素的值 并且 位置+1
            ret = self.data[self.index]
            self.index += 1
            return ret

    def __iter__(self):
        """Python标准规定 迭代器必须是可迭代类型  因此必须实现__iter__方法"""
        return self

class MyData(object):
    """可迭代类型  提供数据"""
    def __init__(self):
        """初始化操作"""
        self.data = [1,2,3,4]
    def __iter__(self):
        """返回 可迭代对象提供的迭代器 """
        md_iter = MyDataIter(self.data)
        return md_iter

# 2 只有在类中实现了__iter__  类的对象才是可迭代类型的   print(isinstance(md, Iterable))
md = MyData()
for i in md:
    print(i)


# 迭代器
md_iter = MyDataIter([1,2,2,2])

print(isinstance(md_iter, Iterable))   # 迭代器是一种可迭代对象
print(isinstance(md_iter, Iterator))

print(isinstance(md, Iterator))