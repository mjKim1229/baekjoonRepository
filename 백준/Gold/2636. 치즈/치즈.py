import sys 
input = sys.stdin.readline 
from collections import deque

n, m = map(int, input().rstrip().split())
graph = [ list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(graph, visited):
    nowDelete = 0 
    afterDelete = 0  
    q = deque()
    q.append((0,0))
    visited[0][0] = True 
    while q: 
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <n and 0<= yy <m and not visited[xx][yy]:
                visited[xx][yy] = True 
                if graph[xx][yy] == 0:
                    q.append((xx,yy))
                else: 
                    graph[xx][yy] = 2 

    for i in range(n):
        for j in range(m):
            #없어질 치즈 공기로 바꿈 
            if graph[i][j] == 2:
                graph[i][j] = 0 
                nowDelete += 1  
            elif graph[i][j] == 1:
                afterDelete +=1 
    #print(nowDelete, afterDelete)
    return nowDelete, afterDelete

    
time = 0 
while True: 
    time +=1 
    visited =[[False] * m for _ in range(n) ]
    nowDelete, afterDelete = bfs(graph, visited)
    if afterDelete == 0:
        print(time)
        print(nowDelete)
        break 
