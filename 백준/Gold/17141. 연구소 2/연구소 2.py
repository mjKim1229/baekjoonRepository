#바이러스 M개 =>상화좌운 퍼짐 
#크기 N X N 
#0: 빈칸, 1: 벽, 2: 바이러스 놓을 수 있는 칸 
import sys 
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
canvirus = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == 2]

combi = list(combinations(canvirus,m)) 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = int(1e9)
for pick in combi:
    q = deque()
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    #virus 놓은 m개 좌표 
    #바이러스 투여 
    for x,y in pick:
        visited[x][y] = True 
        q.append((x,y))

    #2, 0 빈칸처리 => 큐 넣기, 1=> 벽이니까 안됨 
    
    while q: 
        nowX, nowY = q.popleft()
        for i in range(4):
            xx = nowX + dx[i]
            yy = nowY + dy[i]
            if xx<0 or xx>=n or yy<0 or yy>=n: 
                continue

            if visited[xx][yy]:
                continue

            if graph[xx][yy] == 1:
                visited[xx][yy] = True 
                continue
            else: 
                visited[xx][yy] = True
                distance[xx][yy] = distance[nowX][nowY] + 1 
                q.append((xx,yy))
    

    allspread = True 
    singlePickDistance = -1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] != 1:
                allspread = False 
                break 
            singlePickDistance = max(distance[i][j], singlePickDistance)
    
    if allspread:
        answer = min(answer, singlePickDistance)

if answer == int(1e9):
    print(-1)
else: 
    print(answer)