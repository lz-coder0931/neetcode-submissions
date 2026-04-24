class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        freshq = deque()
        rotq = deque()
        rot = set()
        res = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshq.append((i,j))
                if grid[i][j] == 2:
                    rotq.append((i,j))
                    rot.add((i,j))
        if not freshq:
            return 0

        while rotq:
            for k in range(len(rotq)):
                r,c = rotq.popleft()
                for dire in directions:
                    rn = r + dire[0]
                    cn = c + dire[1]
                    if rn in range(m) and cn in range(n) and grid[rn][cn] == 1:
                        grid[rn][cn] = 2
                        rotq.append((rn,cn))
                        freshq.remove((rn,cn))
            res += 1

        if freshq:
            return -1
        else:
            return res





        