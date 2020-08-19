
# 在函数里使用yield函数，无需像迭代器一样定义一个类。使用yield函数后，Python编译器会
# 自动将这个函数识别为迭代器，返回一个可迭代对象，而不是一次全部return，这样做的好处是
# 节省内存空间，并使代码运行更流畅
def fab(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield a
        a, b = b, a+b
        n += 1
