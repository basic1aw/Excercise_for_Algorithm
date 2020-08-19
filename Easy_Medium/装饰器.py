import time

def cal_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('excution time is : {}'.format(end - start))

    return wrapper

def fib(n):
    count = 0
    a = 0
    b = 1
    res = []
    while count < n:
        res.append(a)
        a, b = b, a+b
        count += 1
    print(res)

w = cal_time(fib)
w(10)

# @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作

@cal_time
def fib2(n):
    count = 0
    a = 0
    b = 1
    res = []
    while count < n:
        res.append(a)
        a, b = b, a+b
        count += 1
    print(res)

fib2(10)

# 装饰器同样也可以带参数。

def detail(verbose=False):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if verbose == True:
                print('The function is running well')
            return func(*args,**kwargs)
        return wrapper
    return decorator

newdec = detail(True)
m = newdec(fib)
m(10)

# 类装饰器

class deco():

    def __init__(self,func):
        self._func = func

    def __call__(self):
        print('Calling decoration function...')
        self._func()

@deco
def test():
    print('function to be decorated')

from functools import wraps
def newdec(func):
    @wraps(func)
    def new_wrapper(*args,**kwargs):
        """
        The docstring of new_wrapper...
        """
        print('decorating...')
        return func(*args,**kwargs)
    return new_wrapper

@newdec
def test_2():
    """
    the docstring of test_2
    """
    print('function to be decorated')
