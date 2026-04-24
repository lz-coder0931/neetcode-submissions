class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        visit = set()

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                rw,cl = q.popleft()
                for dr, dc in directions:
                    r = rw+dr
                    c = cl+dc
                    print((r,c))
                    if (r,c) not in visit \
                    and r in range(rows) and c in range(cols) and grid[r][c] =='1':
                        q.append((r,c))
                        print((r,c),r,c)
                        visit.add((r,c))




        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visit:
                    bfs(row, col)
                    # print((row, col))
                    # print(res)
                    res += 1

        return res
