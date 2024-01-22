import sys 
input = sys.stdin.readline 
from collections import deque 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0 
def bfs(distance, visited, i,j):
    global dx, dy, answer  
    q = deque()
    q.append((i,j))
    visited[i][j] = True 
    while q:
        x,y = q.popleft()
        for i in range(4):
            tempX = x + dx[i]
            tempY = y + dy[i]
            if 0<= tempX <n and 0<= tempY <m and graph[tempX][tempY] == 'L' and not visited[tempX][tempY]:
                q.append((tempX,tempY))
                visited[tempX][tempY] = True 
                distance[tempX][tempY] = distance[x][y] + 1 
                answer = max(answer, distance[tempX][tempY])
                # if answer < distance[tempX][tempY]:
                #     print(x,y,tempX,tempY)
                #     print(answer,distance[tempX][tempY])
                #     answer = distance[tempX][tempY]
                


#입력 
n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    row = list(input().rstrip())
    graph.append(row)
    
#육지 찾기 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[False] * m for _ in range(n) ]
            distance = [ [0] * m for _ in range(n) ] 
            bfs(distance, visited, i, j)

print(answer)