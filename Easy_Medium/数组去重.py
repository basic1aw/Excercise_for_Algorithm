# 输入一个有序 int 数组，去重规则：数字 x 的出现次数不超过 x，问去重后数组的最大长度
#
# 样例输入
# 1 1 1 2 2 2 3 3 3
# 样例输出
# 6
def deduplicate():
    arr = list(map(int,input('enter a list separated by space').strip().split(' ')))
    de = set(arr)
    # 利用集合去重
    max_len = 0
    for i in de:
        max_len += min(i,arr.count(i))

    return max_len

print(deduplicate())
