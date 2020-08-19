# 假如1+9+8+198=216,198是216的生成数，输入一个数，求它的最小生成数

def solution(n):
    n_str = str(n)
    big_digit = int(n_str[0])
    # 在一个区间遍历寻找
    left = big_digit * len(n_str) * 10 - len(n_str) * 9
    right = n
    res = n
    if n == 0:
        return 0
        # 特判

    for num in range(left,right):
        num_str = str(num)
        sum = num
        for i in num_str:
            sum += int(i)
        if sum == n and num < res:
            res = num
    return res
# 时间复杂度为O(n/10),空间复杂度为O(1)

num = int(input('enter an int to calculate it\'s min generated number...'))
print(solution(num))
