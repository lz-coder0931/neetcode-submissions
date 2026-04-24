class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])

        pac,atl = set(),set()


        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c,visit,prevheight):
            if r in range(m) and c in range(n) and (r,c) not in visit and heights[r][c] >= prevheight:
                visit.add((r,c))
                for direc in directions:
                    rw = r + direc[0]
                    cl = c + direc[1]
                    dfs(rw,cl,visit,heights[r][c])
            else:
                return

        for col in range(n):
            dfs(0,col,pac,heights[0][col])
            dfs(m-1,col,atl,heights[m-1][col])

        for row in range(m):
            dfs(row, 0,pac, heights[row][0])
            dfs(row,n-1,atl,heights[row][n-1])
        res = []
        #find common
        for cellpac in pac:
            if cellpac in atl:
                res.append(list(cellpac))

        return res
        