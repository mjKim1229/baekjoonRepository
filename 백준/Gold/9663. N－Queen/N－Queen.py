import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
board = [0] * n
count = 0 


def promising(rowNum):
    #print(board)
    for i in range(rowNum): 
        if board[i]== board[rowNum] or abs(board[i]-board[rowNum]) == abs(i-rowNum):
            return False
    return True 

def nqueen(rowNum):
    #print("rowNum",rowNum)
    global count  
    if rowNum == n:
        count+=1 
        return  
    
    for i in range(n): 
        board[rowNum] = i 
        if promising(rowNum) == True:
            nqueen(rowNum+1)
    
nqueen(0)
print(count)
        
