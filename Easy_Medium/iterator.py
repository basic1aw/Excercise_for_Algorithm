"""
创建一个迭代器对象，__iter__()方法是创建一个迭代器，
__next__()是生成下一个迭代器
"""

class myiter:

    def __init__(self,start):
        self.a = start

    def __iter__(self,start):
        return self
        # 返回 self，即myiter这个对象，这个对象实现了next方法，因此可以不断遍历

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x

        else:
            raise StopIteration
            # StopIteration 异常用于标识迭代的完成，防止无限循环

m = myiter(10)
example = iter(m)
for x in example:
    print(x)

# 自定义一个List类，实现对list同样的迭代

class newlist:

    def __init__(self,data):
        self.arr = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            element = self.arr[self.idx]
            self.idx += 1
            return element
        except:
            raise StopIteration
