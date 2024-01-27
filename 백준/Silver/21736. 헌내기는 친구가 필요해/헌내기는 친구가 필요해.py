import sys 
input = sys.stdin.readline 
from collections import deque
 
def bfs(x,y):
    global answer
    visited[x][y] = True 
    q = deque()
    q.append((x,y))
    while q: 
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <n and 0<=yy<m and not visited[xx][yy] and graph[xx][yy] != 'X':
                if graph[xx][yy] == 'P':
                    answer += 1 
                visited[xx][yy] = True
                q.append((xx,yy)) 

n, m = map(int, input().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i,j)
            break
answer = 0 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[False] * m for _ in range(n) ]
bfs(start[0],start[1])

if answer == 0:
    print("TT")
else: 
    print(answer)