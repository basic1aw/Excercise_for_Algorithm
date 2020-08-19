# 作者：牛客902271883号
# 链接：https://www.nowcoder.com/discuss/482606?type=post&order=create&pos=&page=0&channel=666&source_id=search_post
# 来源：牛客网

def check(frame, brick, i):
    tmp_frame = list(frame)
    for j in range(i, i+len(brick)):
        tmp_frame[j] += brick[j-i]

    min_elem = min(tmp_frame)
    for i in range(len(tmp_frame)):
        tmp_frame[i] -= min_elem
    return max(tmp_frame)
    # 可以进一步简化为：return max(tmp_frame) - min_elm
def method_1():
    while True:
        try:
            string_1 = input().strip()
            string_2 = input().strip()

            frame = []
            for s in string_1:
                frame.append(int(s))

            brick = []
            for s in string_2:
                brick.append(int(s))
            # 可以直接用 map函数，大大简化

            res = float('inf')

            for i in range(0, len(frame)-len(brick)+1):
                val = check(frame, brick, i)
                res = min(res, val)

            print(res)
        except:
            break


# 个人思路：遍历相加，然后用最大的数减去最小值。就是暴力模拟法
# 另外，因为题目的意思是每一个砖头的层数不超过9（输入时字符串形式，
# 所以就算10以上也会识别为两个个位数）。
# 如果题目再难一点，砖头层数能>10的话，需要转为列表再相加判断。

def solution(frame,brick):

    n = len(frame)
    m = len(brick)
    min_ = float('inf')
    for i in range(n-m+1):
        new = frame[:i] + str(int(frame[i:m+i])+int(brick))+ frame[m+i:]
        baseline = int(min(new))
        remain = int(max(new)) - baseline
        if remain < min_:
            min_ = remain
    return min_
frame = input()
brick = input()
print(solution(frame,brick))


# 2. 复杂情况下，假设输入改成了列表。基本思路不变，参照solution
def solution2(arr1:list,arr2:list) -> int:
    frame = arr1
    brick = arr2
    n = len(frame)
    m = len(brick)
    min_ = float('inf')
    for i in range(n-m+1):
        tmp = frame.copy()
        for j in range(i,i+m):
            tmp[j] += brick[j-i]
            # brick数组的偏移量就是 -i
        baseline = min(tmp)
        remain = max(tmp) - baseline
        if remain < min_:
            min_ = remain
    return min_

a = list(map(int,list(frame)))
b = list(map(int,list(brick)))
c = [10,2,3,9,17]
d = [3,7,1]
print(solution2(c,d))
