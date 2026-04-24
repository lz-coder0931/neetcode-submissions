class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dire = [[0,1], [0,-1], [1,0], [-1,0]]
        rot = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot.add((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))

        time = 0
        while fresh and rot:
            print(rot)
            print(fresh)
            rotting = set()
            for i, j in rot:
                print(i,j)
                for d in dire:
                    ni, nj = i+d[0], j+d[1]
                    if (0<=ni < len(grid) and 0<=nj < len(grid[0])) and (ni,nj) in fresh and (ni, nj) not in rotting:
                        rotting.add((ni, nj))
                        fresh.remove((ni, nj))
            time+=1
            print('rotting', rotting)
            rot = rotting
            if not rotting:
                return -1
        if time != 0 or not fresh:
            return time
        else:
            return -1








        