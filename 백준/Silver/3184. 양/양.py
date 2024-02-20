# 점 (.) : 빈 칸 
# # : 울타리 
# o : 양 
# v : 늑대 

# 울타리 지나지 않고 다른 칸 이동 가능 
#탈출 : 어떤 영역에서도 속하지 x 

#늑대 < 양 : 양 win , 늑대 out 
#else : 모든 양 먹음 

import sys 
input = sys.stdin.readline 
from collections import deque

#행, 열 
n, m = map(int, input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(n)]

#방향 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

wolf = 'v'
sheep = 'o'

def bfs(x,y):
    global totalSheep, totalWolf
    tempDict = {wolf:0, sheep:0}
    #초기 설정 
    visited[x][y] = True
    q = deque()
    q.append((x,y))

    if graph[x][y] != '.':
        tempDict[graph[x][y]] += 1 

    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <n and 0<= yy<m and not visited[xx][yy] and graph[xx][yy] != '#':
                visited[xx][yy] = True
                q.append((xx,yy))
                if graph[xx][yy] != '.':
                    tempDict[graph[xx][yy]] += 1 
    
    if tempDict[sheep] > tempDict[wolf]:
        totalSheep += tempDict[sheep]
    else: 
        totalWolf += tempDict[wolf]

#main 
visited = [[False] * m for _ in range(n)]

totalWolf , totalSheep = 0,0 
for x in range(n):
    for y in range(m):
        if graph[x][y] != '#' and not visited[x][y]:
            bfs(x,y)

print(totalSheep, totalWolf)