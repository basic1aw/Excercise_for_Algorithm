class Solution:
    def print_array(self , arr ):
        # write code here
        n = len(arr)
        m = len(arr[0])
        count = 0
        res = []
        total = n*m
        m0 = 0
        n0 = 0
        while count < total:
            i = n0
            j = m0
            while j <= m-1 and count < total:
                res.append(arr[i][j])
                count += 1
                j += 1
            i += 1
            j = m-1
            while i <= n-1 and count < total:
                res.append(arr[i][j])
                count += 1
                i += 1
            i = n - 1
            j -= 1
            while j >= m0 and count < total:
                res.append(arr[i][j])
                count += 1
                j -= 1
            i -= 1
            j = m0

            while i >= n0+1 and count < total:
                res.append(arr[i][j])
                count += 1
                i -= 1

            m0 += 1
            n0 += 1
            m -= 1
            n -= 1

        res = list(map(str,res))
        return ','.join(res)

        # 时间复杂度分析：O(n^2), 空间复杂度O(n)

a = Solution()
b = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
c = [[1,2,3,4],[10,11,12,5],[9,8,7,6]]
print(a.print_array(b))
print(a.print_array(c))
