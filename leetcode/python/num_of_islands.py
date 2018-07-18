class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        ans=0
        if grid is None or len(grid)==0:
            return 0
        m=len(grid)
        n=len(grid[0])
        is_visited=[[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if is_visited[i][j]==False and grid[i][j]=="1":
                    ans+=1
                    self.bfs(grid,is_visited,i,j)
        return ans

    def bfs(self,grid,is_visited,i,j):
        m=len(grid)
        n=len(grid[0])
        if i<0 or i>=m or j<0 or j>=n:
            return
        if grid[i][j]!="1" or is_visited[i][j]:
            return
        else:
            is_visited[i][j]=True
        self.bfs(grid,is_visited,i-1,j)
        self.bfs(grid,is_visited,i+1,j)
        self.bfs(grid,is_visited,i,j-1)
        self.bfs(grid,is_visited,i,j+1)


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '1', '1']]
    solution = Solution()
    print(solution.numIslands(grid))