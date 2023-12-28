from collections import deque 

startXRef, startYRef = 0,0
leverXRef, leverYRef = 0,0 
endXRef, endYRef = 0,0
destinationX = [0,1,0,-1]
destinationY = [1,0,-1,0]
row , column = 0,0
newMap = []

def go(visited, startX, startY, find):
    global destinationX, destinationY, row, column, newMap
    q = deque([(startX,startY,0)])
    visited[startX][startY] = True 
    while q:
        x,y,time = q.popleft()
        for i in range(4):
            tempX = x + destinationX[i]
            tempY = y + destinationY[i]
            if 0<=tempX<row and 0<=tempY <column and not visited[tempX][tempY] and newMap[tempX][tempY] != 'X':
                if newMap[tempX][tempY] == find:
                    return time +1  
                visited[tempX][tempY] = True 
                q.append((tempX,tempY,time+1))
    return -1 
        

        

def solution(maps):
    global startXRef, startYRef, leverXRef, leverYRef,endXRef, endYRef, row, column, newMap
    row = len(maps)
    column = len(maps[0])
    for i in range(row):
        newMap.append(list(maps[i]))
        for j in range(column):
            temp = newMap[i][j]
            if temp == "S":
                startXRef, startYRef = i,j 
            elif temp == "L": 
                leverXRef, leverYRef =i,j 
            elif temp == "E":
                endXRef, endYRef = i,j 
    visited = [[False]*column for _ in range(row)]
    leverTime = go(visited,startXRef, startYRef,"L")
    print("leverTime",leverTime)
    if leverTime == -1: 
        return -1 
    visited = [[False]*column for _ in range(row)]
    endTime = go(visited,leverXRef, leverYRef,"E")
    print(leverXRef, leverYRef)
    print("endTime",endTime)
    if endTime == -1:
        return -1 
    return leverTime + endTime