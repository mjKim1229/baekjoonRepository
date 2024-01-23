import sys 
input = sys.stdin.readline 
from collections import deque 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0  
def bfs(graph,visited,x,y):
    count = 1 
    global dx, dy 
    q = deque()
    q.append((x,y))
    visited[x][y] = True  
    while q: 
        x, y = q.popleft()
        for i in range(4):
            tempX = x + dx[i]
            tempY = y + dy[i]
            if 0<= tempX <n and 0<= tempY <m and graph[tempX][tempY] == -1 and not visited[tempX][tempY]:
                q.append((tempX,tempY))
                count += 1 
                visited[tempX][tempY] = True 
    return count 

n, m, k = map(int, input().rstrip().split())

#쓰레기 : -1 , 기본 : 0 
graph = [ [0] * m for _ in range(n) ]
trashes = []
for _ in range(k):
    x, y = map(int, input().rstrip().split())
    graph[x-1][y-1] = -1   
    trashes.append((x-1,y-1))


answer = 0 
visited = [[False] * m for _ in range(n)]
for x, y in trashes:
    if not visited[x][y]:
        count = bfs(graph,visited, x,y)
        answer = max(count, answer)
    

print(answer) 