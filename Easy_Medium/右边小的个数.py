def small(arr):
    res = []
    for i in range(len(arr)):
        count = 0
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count += 1
        res.append(count)
    return res

a = [5,4,3,2,1]
print(small(a))
