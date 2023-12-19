def changeDirection(dir): 
    print("dir",dir)
    if dir == 3:
        dir = 0  
        return 0 
    else: 
        dir +=1 
        return dir 
    
def solution(n):
    dir = 0 
    x, y = 0,0
    count = 1 
    
    directionX = [0,1,0,-1]
    directionY = [1,0,-1,0]
    
    answer = [[0]*n for _ in range(n)]     
    answer[x][y] = count 
    count +=1 
    
    while(True):
        if count > n*n: 
            break
        tempX = x + directionX[dir]
        tempY = y + directionY[dir]
        print(tempX,tempY,dir)
        if 0<= tempX <n and 0<= tempY <n: 
            if answer[tempX][tempY] == 0:
                x, y = tempX, tempY
                answer[x][y] = count
                count +=1
            else: 
                dir = changeDirection(dir)
        else: 
            dir = changeDirection(dir)
    print(answer)

    return answer
