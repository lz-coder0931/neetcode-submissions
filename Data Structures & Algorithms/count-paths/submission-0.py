class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    mem[i][j] = 1
                else:
                    mem[i][j] = mem[i-1][j]+mem[i][j-1]
        return mem[-1][-1]