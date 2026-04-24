class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direc = [[-1, 0], [0,-1], [1,0],[0,1]]
        visited = set()
        def btrack(x,y,n):
            if n==len(word):
                return True
            if not(x in range(0, len(board)) and y in range(0, len(board[0]))):
                return False
            if board[x][y] != word[n] or (x,y) in visited:
                return False
            visited.add((x,y))
            for rd, cd in direc:
                if btrack(x+rd, y+cd, n+1):
                    return True
            visited.remove((x,y))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if btrack(i,j,0):
                    return True
        return False



