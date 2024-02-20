#연구소 N X M 
# 벽 3개 
#0: 빈칸, 1: 벽 , 2: 바이러스 
import sys ,copy
input = sys.stdin.readline
from collections import deque, Counter 
from itertools import combinations

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

wallCanLoc = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == 0]
viruses = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == 2]

combi = list(combinations(wallCanLoc,3)) 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    #초기 처리 
    visited[x][y] = True
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx<0 or xx>=n or yy<0 or yy>=m:
                continue
            if visited[xx][yy]:
                continue
            #벽이면 
            if new_graph[xx][yy] == 1:
                visited[xx][yy] = True
                continue
            else: 
                visited[xx][yy] = True
                new_graph[xx][yy] = 2 
                q.append((xx,yy))

answer = 0 
for walls in combi:
    new_graph = copy.deepcopy(graph)
    #벽 세우기 
    for x,y in walls:
        new_graph[x][y] = 1
    
    #방문 
    visited = [[False] * m for _ in range(n)]

    #바이러스 출발점 마다 확산
    for virus in viruses:
        x,y = virus
        bfs(x,y) 
   
    tmpAnswer = 0 
    for x in range(n):
        for y in range(m):
            if new_graph[x][y] ==0:
                tmpAnswer += 1 
    answer = max(answer, tmpAnswer)

    #벽 철거 
    for x,y in walls:
        new_graph[x][y] = 0 

print(answer)