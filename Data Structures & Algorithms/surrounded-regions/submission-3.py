class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visit = deque()
        land = deque()
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        flag = True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visit:
                    q.append((i,j))
                    land.append((i,j))
                    visit.append((i,j))
                    #print(land)
                while q:
                    row, col = q.popleft()
                    print('loc', row,col)
                    if row == 0 or col ==0 or row == len(board)-1 or col == len(board[0])-1:
                        flag = False
                        print(row, col, flag)
                    for rd, cd in directions:
                        r, c = row+rd, col+cd
                        if r in range(len(board)) and c in range(len(board[0])) and (r,c) not in land and board[r][c]=='O':
                            q.append((r,c))
                            land.append((r,c))
                            visit.append((r,c))
                            print('added')
                    print(land)
                if flag:
                    for x,y in land:
                        print(x,y)
                        board[x][y] = 'X'

                land.clear()
                flag=True



        