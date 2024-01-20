import sys 
input = sys.stdin.readline 
import math 
r, c, t = map(int, input().rstrip().split())


graph = []
cleaner = []
for i in range(r):
    row = list(map(int, input().rstrip().split()))
    if row[0] == -1:
        cleaner.append(i)
    graph.append(row) 

for _ in range(t):
    #미세먼지 확산 
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    #초만큼 반복처리 
    blowedDust = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            singleBlow = math.trunc(graph[i][j] / 5)
            for k in range(4):
                tempX = i + dx[k]
                tempY = j + dy[k]
                if 0<= tempX <r and 0<= tempY <c and graph[tempX][tempY] != -1:
                    blowedDust[tempX][tempY] += singleBlow
                    graph[i][j] -= singleBlow

    for i in range(r):
        for j in range(c):
            graph[i][j] += blowedDust[i][j]


    #정화 
    #위 : 동 북 서 남 
    dir = 0
    nowX = cleaner[0]
    nowY = 0
    beforeVaue = 0
    while True:
        tempX = nowX + dx[dir]
        tempY = nowY + dy[dir]
        if 0<=tempX<r and 0<= tempY <c: 
            if graph[tempX][tempY] == -1:
                break 
            forNextValue = graph[tempX][tempY]
            graph[tempX][tempY] = beforeVaue
            beforeVaue = forNextValue
            nowX, nowY = tempX, tempY
        else: 
            dir = (dir - 1) % 4 

    #아래 : 동 남 서북 
    dir = 0
    nowX = cleaner[1] 
    nowY = 0
    beforeVaue = 0

    while True:
        tempX = nowX + dx[dir]
        tempY = nowY + dy[dir]
        if 0<=tempX<r and 0<= tempY <c: 
            if graph[tempX][tempY] == -1:
                break 
            forNextValue = graph[tempX][tempY]
            graph[tempX][tempY] = beforeVaue
            beforeVaue = forNextValue
            nowX, nowY = tempX, tempY
        else: 
            dir = (dir + 1) % 4 

        
    
    
    
answer = 0 
for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            answer += graph[i][j]
print(answer) 