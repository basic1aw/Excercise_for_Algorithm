class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 思路：把二维矩阵视为无向图，遍历节点直到遇到'0'或者边界处，则返回至起始节点的相邻节点
        # 即上下左右节点重新递归DFS。同时，根据题意，将访问过的节点标记为0，这样就能判断连通大陆数
        # 1 为大陆，而DFS只放问连续的1，即为岛屿。
        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            # 访问过的节点直接标记为0，当然也可以标记为其他值。
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        return count

        # 时间复杂度为：O（MN）,空间复杂度：递归栈空间O(MN)，最坏情况是全为1，则要递归访问全部节点。
