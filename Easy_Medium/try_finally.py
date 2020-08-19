def test():
    try:
        a = 3
        return a
    except:
        pass
    finally:
        a += 3
        return a

# 1. 当try代码块中有return语句时，先执行return语句再执行finally代码块
# 2. 当finally中也有return语句，且return的是同一个变量，那么只会返回
# try中的变量对应的值，finally中对变量进行修改后也不会影响返回的值
