def solution(board):
    straightX = [0,1,0,-1]
    straightY = [1,0,-1,0]
    crossX = [-1,-1,1,1]
    crossY = [-1,1,-1,1]
    boardLength = len(board)
    danger = [[0]*boardLength for _ in range(boardLength)]
    for x in range(boardLength): 
        for y in range(boardLength):
            if board[x][y] ==1:
                for i in range(4):
                    tempX = x + straightX[i]
                    tempY = y + straightY[i]
                    if 0<=tempX<boardLength and 0<=tempY<boardLength and board[tempX][tempY] ==0:
                        danger[tempX][tempY] = 1 
                    tempX = x + crossX[i]
                    tempY = y + crossY[i]
                    if 0<=tempX<boardLength and 0<=tempY<boardLength and board[tempX][tempY] ==0:
                        danger[tempX][tempY] = 1 
    print(board)
    dangerCount = 0 
    for x in range(boardLength): 
        for y in range(boardLength): 
            if danger[x][y] == 1: 
                dangerCount +=1
    
    for x in range(boardLength): 
        for y in range(boardLength): 
            if board[x][y] == 1:
                dangerCount += 1
     
    
    return boardLength*boardLength - dangerCount
                
    