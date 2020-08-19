def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for i in range(m)]
    dp[0][0] = grid[0][0]
# 用dp[i][j]表示坐标为(i,j)的最小路径和
    for i in range(1,m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
# 以上为初始条件，因为最边上的两边最小路径是一直往右或往左，所以容易求得两边的最小路径

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
# 因为任意一点(i,j)的最小路径和肯定是其左边和上边的最小路径和的最小值然后加上该点的数值
# 其实就是数学归纳法，用dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]表示
    return dp[-1][-1]
