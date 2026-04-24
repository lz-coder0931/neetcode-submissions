class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col) -> int:
            q = deque()
            q.append((row, col))
            visit.add((row, col))
            area = 1
            while q:
                row_q, col_q = q.popleft()
                for rd, cd in directions:
                    r = row_q + rd
                    c = col_q + cd
                    if  r in range(rows) and c in range(cols) \
                    and grid[r][c] == 1 and (r, c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        area += 1
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visit:
                    area = bfs(row, col)
                    res = max(res, area)
        
        return res




        