"""
华为2020.8.19机试题
输入M,N表示有M行N列的一个矩阵，按照顺时针螺旋的方式计数（从1开始）
当坐标(i,j)对应的计数的个位数为7且十位数是奇数则将其坐标作为一个数组(即[i,j])加入team
是在leetcode的螺旋矩阵题目上改编的。
题目条件给出了M和N的取值范围均在[10,1000]，但其实还是需要手动判断！！！
"""
while True:
    try:
        m, n = map(int,input('').split(' '))
        count = 1
        team = []
        total = n*m
        m0 = 0
        n0 = 0
        while count <= total:
            i = n0
            j = m0
            while j <= m-1 and count <= total:
                if count%10 == 7 and (count//10%2 != 0):
                    team.append([i,j])
                count += 1
                j += 1
            i += 1
            j = m-1

            while i <= n-1 and count <= total:
                if count%10 == 7 and (count//10%2 != 0):
                    team.append([i,j])
                count += 1
                i += 1
            i = n - 1
            j -= 1

            while j >= m0 and count <= total:
                if count%10 == 7 and (count//10%2 != 0):
                    team.append([i,j])
                count += 1
                j -= 1
            i -= 1
            j = m0

            while i >= n0+1 and count < total:
                if count%10 == 7 and (count//10%2 != 0):
                    team.append([i,j])
                count += 1
                i -= 1

            m0 += 1
            n0 += 1
            m -= 1
            n -= 1

        print(str(team).replace(' ',''))
        # 傻逼牛客，需要输出字符串格式的数组，列表转换成字符串后，会出现空格!!
    except:
        print('[]')


# 2. 牛客大神100% AC版本
作者：牛客902271883号
链接：https://www.nowcoder.com/discuss/482606?type=post&order=create&pos=&page=0&channel=666&source_id=search_post
来源：牛客网

def isValid(num):
    if num < 10:
        return False
    ge = num % 10

    tmp = num // 10
    shi = tmp % 10

    if ge == 7 and shi % 2 == 1:
        return True
    else:
        return False


while True:
    try:
        m, n = map(int, input().split())

        if m < 10&nbs***bsp;n < 10:
            print('[]')
            continue

        maze = [[False for _ in range(n)] for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        total = m * n
        mask = [0 for _ in range(total)]

        cur_x, cur_y = 0, 0
        idx = 0
        res = []

        for i in range(total):

            if isValid(i+1):
                res.append([cur_x, cur_y])

            maze[cur_x][cur_y] = True

            nxt_x = cur_x + directions[idx][0]
            nxt_y = cur_y + directions[idx][1]

            if not (0 <= nxt_x < m and 0 <= nxt_y < n and not maze[nxt_x][nxt_y]):
                idx += 1
                idx %= 4

            cur_x += directions[idx][0]
            cur_y += directions[idx][1]

        string = '['
        for idx, (x, y) in enumerate(res):
            if idx != len(res) - 1:
                tmp = '[{},{}],'.format(x, y)
                string += tmp
            else:
                tmp = '[{},{}]]'.format(x, y)
                string += tmp
        print(string)
    except:
        break
