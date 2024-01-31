#크기 작음 : 먹 o 이동 o
#크기 같음 : 먹 x 이동 o + 크기 1 증가 
#크기 큼 : 먹 x 이동 x 

#먹을 수 있는 물고기 x : 도움 요청 
#먹을 수 있는 물고기 1 : 먹음 
#먹을 수 있는 물고기 2이상 : 거리가 가장 가까운 
#거리가 가까운 물고기 많다면 => 위 -> 왼쪽 
import sys 
input = sys.stdin.readline 
from collections import deque

def bfs(x,y,visited):
    global sharkBig, graph, eatCount, time
    priorityX, priorityY, priorityDistance = int(1e9), int(1e9), int(1e9)
    visited[x][y] = True 
    q = deque()
    q.append((x,y,0))
    graph[x][y] = 0 
    while q: 
        nowX, nowY, nowDistance = q.popleft()
        for i in range(4):
            xx = nowX + dx[i]
            yy = nowY + dy[i]
            if 0<= xx <n and 0<=yy<n and not visited[xx][yy]:
                #print(xx,yy,graph[xx][yy],sharkBig)
                #빈칸 , 같은 크기 : 지나감 
                if graph[xx][yy] == 0 or graph[xx][yy] == sharkBig:
                    q.append((xx,yy,nowDistance+1))
                    visited[xx][yy] = True
                #먹을 수 있는 고기 
                elif graph[xx][yy] < sharkBig:
                    #xx,yy까지의 거리 
                    tempDistance = nowDistance + 1
                    q.append((xx,yy,tempDistance))
                    visited[xx][yy] = True 
                    #거리가 최소거리보다 짧다면 
                    if tempDistance < priorityDistance:
                        priorityX, priorityY, priorityDistance = xx, yy, tempDistance
                    elif tempDistance == priorityDistance:
                        #위에 있는 게 우선순위 
                        if xx < priorityX:
                            priorityX, priorityY, priorityDistance = xx, yy, tempDistance
                        elif xx == priorityX:
                            #왼쪽에 있는 게 우선순위 
                            if yy < priorityY:
                                priorityX, priorityY, priorityDistance = xx, yy, tempDistance
    if priorityDistance != int(1e9):
        graph[priorityX][priorityY] = 0 
        eatCount +=1 
        time += priorityDistance
        #print(priorityX,priorityY,priorityDistance)
        return (priorityX,priorityY,priorityDistance)    
    else: 
        return (int(1e9), int(1e9), int(1e9))
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input().rstrip())
graph = []
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    graph.append(row)
    for j in range(n):
        if graph[i][j] == 9:
            start = (i,j)

sharkBig = 2
eatCount = 0 
time = 0 
parX, parY = start[0], start[1]
while True:
    visited = [ [False] * n for _ in range(n) ]
    tempParX, tempParY , tempParDistance = bfs(parX, parY, visited)
    if (tempParX, tempParY , tempParDistance) == (int(1e9), int(1e9), int(1e9)):
        break 
    parX, parY = tempParX, tempParY
    if eatCount == sharkBig:
        sharkBig += 1 
        eatCount = 0 

print(time)
