
def spiral_print(arr):
    res = []
    m1 = 0
    n1 = 0
    m2 = len(arr) - 1
    n2 = len(arr[0]) - 1
    total = len(arr) * len(arr[0])
    count = 0
    visited = []
    # 需要用一个列表存储访问过的坐标
    while count < total:
        for i in range(n1,n2+1):
            if [m1,i] not in visited:
                res.append(arr[m1][i])
                visited.append([m1,i])
                count += 1


        for j in range(m1+1,m2+1):
            if [j,n2] not in visited:
                res.append(arr[j][n2])
                visited.append([j,n2])
                count += 1

        for i in range(n2-1,n1-1,-1):
            if [m2,i] not in visited:
                res.append(arr[m2][i])
                visited.append([m2,i])
                count += 1

        for j in range(m2-1,m1,-1):
            if [j,n1] not in visited:
                res.append(arr[j][n1])
                visited.append([j,n1])
                count += 1

        m1 += 1
        m2 -= 1
        n1 += 1
        n2 -= 1

    res = list(map(str,res))
    print(','.join(res))

# 时间复杂度O(n^2),因为还有一个in判断，系数很大，
# 空间复杂度O(2n)

b = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
c = [[1,2,3,4],[10,11,12,5],[9,8,7,6]]

spiral_print(b)
spiral_print(c)
