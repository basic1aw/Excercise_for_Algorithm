# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000

# 1. 奇数回文串，即从中间往两边遍历比较
# 2. 偶数回文串，即起始位置为左右两边第一个字符
def longest_panlindrome(str):
    n = len(str)
    max_len = 0
    if n <= 1:
        return str

    for i in range(1,n):
        odd_left = i
        odd_right = i
        while odd_left >= 0 and odd_right <= n-1:
            if str[odd_left] != str[odd_right]:
                break
            else:
                odd_left -= 1
                odd_right += 1
        odd_len = odd_right - odd_left - 1

        even_left = i - 1
        even_right = i
        while even_left >= 0 and even_right <= n -1:
            if str[even_left] != str[even_right]:
                break
            else:
                even_left -= 1
                even_right += 1
        even_len = even_right - even_left - 1
        idx = []
        if even_len > odd_len:
            if even_len > max_len:
                max_len = even_len
                l = even_left+1
                r = even_right-1
        else:
            if odd_len > max_len:
                max_len = odd_len
                l = odd_left+1
                r = odd_right-1

    return str[l:r+1]

while True:
    str = input('input a string:')
    print(longest_panlindrome(str))
