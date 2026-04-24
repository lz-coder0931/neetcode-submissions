class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        m = len(grid)
        n = len(grid[0])

        def bfs(q, d):
            visit = set()
            while q:
                i, j, d = q.popleft()
                visit.add((i,j))
                for direc in directions:
                    r = i + direc[0]
                    c = j + direc[1]
                    if r in range(m) and c in range(n) and grid[r][c] > 0 and (r,c) not in visit:
                        grid[r][c] = min(grid[r][c], d)
                        q.append((r,c, d+1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q = deque()
                    q.append((i,j,1))
                    bfs(q, 1)






        