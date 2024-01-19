import sys 

#0이 있냐 : True , 0이 없냐 : False 
def checkBoundary(graph,x,y):
    flag = False 
    for i in range(4):
        tempX = x + dx[i]
        tempY = y + dy[i]
        if 0<=tempX<n and 0<=tempY<m and graph[tempX][tempY] == 0:
            flag = True 
    return flag 

n, m = map(int,input().rstrip().split())

#0: 북, 1: 동, 2:남 , 3: 서 
x, y , dir = map(int,input().rstrip().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = []
for _ in range(n):
    row = list(map(int,input().rstrip().split()))
    graph.append(row)


while True:
    if graph[x][y] == 0: 
        graph[x][y] = -1 
    if checkBoundary(graph,x,y):
        dir = (dir - 1) % 4
        frontX = x + dx[dir]
        frontY = y + dy[dir]
        if 0<= frontX < n and 0<= frontY <m:
            if graph[frontX][frontY] == 0:
                x, y = frontX, frontY
                graph[x][y] = -1 
    else:
        backX = x - dx[dir]
        backY = y - dy[dir]
        if 0<= backX <n and 0<=backY<m:
            if graph[backX][backY] == 1:
                break 
            else: 
                x ,y = backX, backY 
                graph[x][y] = -1  
 


cleanCount = 0 
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            cleanCount +=1 

print(cleanCount)

