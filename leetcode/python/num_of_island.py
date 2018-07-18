class Solution(object):

    def num_islands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]  # m*n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    def bfs(self, grid, visited, x, y, m, n):
        dz = list(zip([1, 0, -1, 0], [0, 1, 0, -1]))
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.is_valid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[np[0]][np[1]] = True
                    queue.append(np)

    def dfs(self, grid, visited, x, y):
        if x<0 or x>=len(grid):
            return
        if y<0 or y>=len(grid[0]):
            return
        if grid[x][y]!= '1' or visited[x][y]:
            return
        visited[x][y]=True
        self.dfs(grid, visited, x-1, y)
        self.dfs(grid, visited, x+1, y)
        self.dfs(grid, visited, x, y-1)
        self.dfs(grid, visited, x, y+1)


    def is_valid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '1', '1']]
    solution = Solution()
    print(solution.num_islands(grid))