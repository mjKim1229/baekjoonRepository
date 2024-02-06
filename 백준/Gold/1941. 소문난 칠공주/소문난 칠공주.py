import sys 
input = sys.stdin.readline 
from itertools import combinations
from collections import deque

graph = [list(input().rstrip()) for _ in range(5)]

totalLoc = [(x,y) for x in range(5) for y in range(5)]

combi = list(combinations(totalLoc,7)) 
answer = 0 
for pick in combi:
    #숫자 pick 
    s = 0 
    y = 0 
    for a, b in pick:
        if graph[a][b] == 'S':
            s +=1 
        else: 
            y += 1 
    if s <= y:
        continue

    visited = [[False] * 5 for _ in range(5)]
    x, y = pick[0][0], pick[0][1]

    q = deque()
    q.append((x,y))
    visited[x][y] = True

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = 1 

    while q: 
        nowX, nowY = q.popleft()
        for i in range(4):
            xx = nowX + dx[i]
            yy = nowY + dy[i]
            if 0<= xx <5 and 0<= yy<5 and not visited[xx][yy] and (xx,yy) in pick:
                q.append((xx,yy))
                visited[xx][yy] = True 
                count +=1 
    if count == 7:
        answer +=1 
print(answer)
    