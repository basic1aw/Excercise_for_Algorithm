# 统计一个字符串中每个字母出现次数，并以字符大小排序。
# 注意：该字符串只包含字母，大小写
# 然后以字符+该字符出现次数输出。如'abxa'--'a2b1x1'
a = input("enter a string:...")
count = [0] * (ord('z') - ord('A'))
for i in a:
    if 'A'<=i<='Z' or 'a'<=i<='z':
        # 考虑代码robustness, 如果有其他非字母字符，直接跳过不统计
        count[ord(i)-ord('A')] += 1

res = ''
for i in range(len(count)):
    if count[i] != 0:
        res += chr(i + ord('A')) + str(count[i])

print(res)

# 时间复杂度 O(n+54)
# 空间复杂度 O(52+2n) O(n)


# Solution 2/
# 用哈希表来将出现的字母和相应的此处作为键值对存储起来, 用 ord 转为ASCII 值
# hashmap = {}
# for i in a:
#     hashmap[ord(i)-ord('A')] = hashmap.get(ord(i)-ord('A'),0) + 1
#
# ans = ''
# for k,time in hashmap.items():
#     ans += chr(k+ord('A')) + str(time)
# print(ans)
