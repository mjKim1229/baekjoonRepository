import sys 
input = sys.stdin.readline 
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(visited, touchCounts):
    meltCandidates = set()
    global dx, dy 
    visited[0][0] = True 
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            tempX = x + dx[i]
            tempY = y + dy[i]
            if 0<= tempX <n and 0<= tempY <m and not visited[tempX][tempY]:
                if graph[tempX][tempY] == 0:
                    visited[tempX][tempY] = True
                    q.append((tempX,tempY))
                elif graph[tempX][tempY] == 1:
                    #visited[tempX][tempY] = True
                    meltCandidates.add((tempX,tempY))
                    touchCounts[tempX][tempY] +=1
    
    
    #print(meltCandidates)
    #print(touchCounts) 
    #녹이기 
    count = 0 
    for x,y in meltCandidates:
        if touchCounts[x][y] >=2:
            graph[x][y] = 0
            count +=1    
    return count               

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    row = list(map(int, input().rstrip().split()))
    graph.append(row)

time = 0 
while True: 
    time +=1 
    visited =[ [False] * m for _ in range(n) ]
    touchCounts = [ [0] * m for _ in range(n) ]
    count = bfs(visited,touchCounts)
    if count == 0:
        break 

print(time-1)
