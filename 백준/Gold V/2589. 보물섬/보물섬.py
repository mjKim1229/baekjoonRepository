# L 육지 , W 바다 
# 상하좌우 육지로만 
# 한칸 한시간 
# 최단거리로 이동하는 데 있어 가장 긴 시간 걸리는 육지 2곳 
import sys 
input = sys.stdin.readline 
from collections import deque 

n, m = map(int, input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(n)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,visited):
    global answer 
    visited[x][y] = True
    q = deque()
    q.append((x,y,0))
    while q: 
        x, y, time = q.popleft()
        answer = max(answer, time)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <n and 0<= yy <m and not visited[xx][yy]:
                if graph[xx][yy] == 'L':
                    visited[xx][yy] = True 
                    q.append((xx,yy,time+1))

answer = 0 
for x in range(n):
    for y in range(m):
        if graph[x][y] == 'L':
            visited = [[False] * m for _ in range(n)]
            bfs(x,y,visited)

print(answer)