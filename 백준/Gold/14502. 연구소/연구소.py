import sys 
input = sys.stdin.readline 
from collections import deque
from itertools import combinations
import copy
#0: 빈칸 , 1: 벽 2: 바이러스 
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

#virus 저장 
virus = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == 2]
blanks = [(x,y) for x in range(n) for y in range(m) if graph[x][y] ==0]

wallcombi = list(combinations(blanks,3)) 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0 

for pick in wallcombi:
    
    #안전 영역 
    safeCount = 0 
    #temp로 바이러스 전파 
    temp = copy.deepcopy(graph)
    visited = [[False] * m for _ in range(n)]
    
    #벽 세우기 
    for x, y in pick:
        temp[x][y] = 1 
    
    #초기 바이러스 
    q = deque()
    for x, y in virus:
        q.append((x,y))
        visited[x][y] = True 

    #bfs 
    while q: 
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy]:
                #벽 말고 빈칸, 바이러스는 확산 가능 
                if temp[xx][yy] != 1:
                    visited[xx][yy] = True
                    temp[xx][yy] = 2
                    q.append((xx,yy))
    
    #안전지대 count 
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safeCount +=1 
    answer = max(answer, safeCount)
  
    #벽 원상태로 
    for x,y in pick:
        temp[x][y] = 0 

print(answer)
