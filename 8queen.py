N=4
board= [[0 for i in range(N)] for i in range(N)]

def check_Column(board,row,column):
    for i in range(row,-1,-1): #check every row if queen is there or not
        if board[i][column]==1:#checking in the decremented row of same column
            return False
    return True
def check_Diagonal(board,row,column):
    #diagonally moving towards top left
    for i,j in zip(range(row,-1,-1),range (column,-1,-1)):
        if board[i][j]==1:
         return False
        #diagonally moving towards top right
    for i,j in zip(range(row,-1,-1),range (column,N)):
        if board[i][j]==1:
         return False
    return True
    #backtracking logic
def nQueens(board,row):
    #since list of list is zero indexed
     if row==N:
      return True
     for i in range(N):
      if (check_Column(board,row,i)==True and check_Diagonal(board,row,i)==True): #checking column
       board[row][i]=1 # 1 for placing queens
       if nQueens(board,row+1):#next queenplacing
           return True
       board[row][i]=0
     return False
nQueens(board,0)
for row in board:
    print(row)   