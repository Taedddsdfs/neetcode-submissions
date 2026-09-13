class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        

        def capture(r,c):
            if (r not in range(m) or c not in range(n) or board[r][c]!="O"):
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r,c-1)
        
        for r in range(m):
            if board[r][0] == "O":
                capture(r,0)
            if board[r][n-1] =="O":
                capture(r,n-1)
        for c in range(n):
            if board[0][c] == "O":
                capture(0, c)
            if board[m - 1][c] == "O":
                capture(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c]= "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"