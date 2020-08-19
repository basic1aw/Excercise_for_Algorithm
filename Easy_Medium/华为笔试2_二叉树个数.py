#
# 题目大意：二叉树有n个节点，每个节点的深度已知（代码中depth），让你计算该树总共有多少种可能的形状。
# 例如 depth为[0, 1]可能两种情况： 父节点和左孩子 、 父节点和右孩子
# 返回的值需要对 10**9+7 取模
# 坑点： 下一层的个数可能会大于上一层个数的两倍，return 0
# 思路：组合排列。其中输入的数表示节点所在深度，自然想到用列表或者哈希表来
# 存储节点深度和节点数。
# 从第1层遍历至max_depth+1层，其中第 i 层的节点数为Ni,第i-1层的结点数为Ni-1
# 则第i层的所有组合为，C(2Ni-1,Ni)，抽象出来就是第i层总共有2Ni-1个位置，将
# Ni个节点放入这2Ni-1个位置的组合。

import os

n = int(input())
depth = [int(d) for d in input().split()]

M = 10 ** 9 + 7


def combination(n, k):
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    # 对组合公式的化简
    top = 1
    for i in range(n, n - k, -1):
        top *= i

    down = 1
    for i in range(1, k + 1):
        down *= i

    return (top // down) % M


def helper():
    if n == 0:
        return 0

    max_depth = max(depth)
    depth_count = [0] * (max_depth + 1)

    for d in depth:
        depth_count[d] += 1
    # 用一个列表来记录每一层节点的个数，下标对应深度，值对应结点数

    for i in range(max_depth):
        if 2 * depth_count[i] < depth_count[i + 1]:
            return 0
        # 二叉树隐藏条件，即n+1层的结点数<= n层的节点数 * 2

    r = 1
    for i in range(1, max_depth + 1):
        r *= combination(2 * depth_count[i - 1], depth_count[i])
        r %= M

    return r


print(helper())
