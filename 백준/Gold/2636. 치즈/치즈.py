import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(visited):
    cnt = 0 
    global dx, dy 
    q = deque()
    q.append((0,0))
    visited[0][0] = True 
    while q: 
        x, y = q.popleft()
        for i in range(4):
            tempX = x + dx[i]
            tempY = y + dy[i]
            if 0<= tempX <n and 0<= tempY <m and not visited[tempX][tempY]:
                if graph[tempX][tempY] == 0:
                    q.append((tempX,tempY))
                    visited[tempX][tempY] = True
                elif graph[tempX][tempY] == 1: 
                    visited[tempX][tempY] = True 
                    graph[tempX][tempY] = 0
                    cnt += 1 
    return cnt 


n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    row = list(map(int, input().rstrip().split()))
    graph.append(row)


time = 0 
answer = []
while True: 
    time +=1 
    visited =[[False] * m for _ in range(n)]
    cnt = bfs(visited)
    if cnt == 0:
        break 
    answer.append(cnt)

print(time-1)
print(answer[-1])