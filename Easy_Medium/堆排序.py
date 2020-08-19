class BinHeap:
# 可以用二叉堆来实现优先队列，即二叉堆节点的值为优先级，这样可以根据优先级
# 来实现优先出队，保证出队和入队复杂度为O(logN)
    def __init__(self):
        self.size = 0
        self.HeapList = [None]

    def down(self,i):
        while 2 * i <= self.size:
            mc = self.MinChild(i)
            if self.HeapList[mc] < self.HeapList[i]:
                self.HeapList[mc], self.HeapList[i] = self.HeapList[i], self.HeapList[mc]

            i = mc

    def MinChild(self,i):
        if 2 * i + 1 > self.size:
            return 2 * i

        else:
            if self.HeapList[2*i+1] > self.HeapList[2*i]:
                return 2 * i

            else:
                return 2*i+1

    def up(self,i):
        while i//2 > 0:
            if self.HeapList[i] < self.HeapList[i//2]:
                tmp = self.HeapList[i]
                self.HeapList[i] = self.HeapList[i//2]
                self.HeapList[i//2] = tmp
            i = i // 2

    def insert(self,item):
        self.HeapList.append(item)
        self.size += 1
        self.up(self.size)

    # 最大堆增加一个元素节点的复杂度O（logN）

    def delMin(self):
        val = self.HeapList[1]
        self.HeapList[1] = self.HeapList.pop()
        self.size -= 1
        self.down(1)
        return val
    # 删除一个最小值复杂度O（logN）


    def BuildHeap(self,arr):
        self.size = len(arr)
        self.HeapList = [None] + arr[:]
        i = len(arr)//2
        while i > 0:
            self.down(i)
            i -= 1
        return self.HeapList

    def sort(self):
        # 最小堆，则每次把最小值放在List末尾，然后在[:n-1]范围内找出最小值，同时要更新size-1
        # 直到n-1 = 1
        # 其实和DelMin()函数的思想一样
        n = self.size
        for i in range(n,0,-1):
            self.HeapList[i],self.HeapList[1] = self.HeapList[1],self.HeapList[i]
            self.size -= 1
            self.down(1)
        return self.HeapList[1:]
        # 切片复杂度为O（k）,因此还可以继续优化,即直接从下表为0开始存储数据
        # 父子节点关系为 i 2*i+1 2*i+2
        # down(1)复杂度为O（logN），BuildHeap()复杂度为O（N）,总的复杂度O（NlogN）
import random
p = []
for x in range(11):
    p.append(random.randint(-100,100))
a = BinHeap()
a.BuildHeap(p)
print(a.sort())
