#0: 빈칸 1: 벽 2: 바이러스
import sys 
input = sys.stdin.readline 
from itertools import combinations
#방향 
destinationX = [0,1,0,-1]
destinationY = [1,0,-1,0]

#입력 
row, column = map(int,input().rstrip().split())
graph = []

for _ in range(row):
    tempRow = list(map(int,input().rstrip().split())) 
    graph.append(tempRow)

#벽 세울 위치 3곳 선택 
wallCanList = [(x,y) for x in range(row) for y in range(column) if graph[x][y] ==0]
wallPickThree = list(combinations(wallCanList,3))

#바이러스 위치 
virusList = []
for i in range(row): 
    for j in range(column): 
        if graph[i][j] == 2: 
            virusList.append((i,j))

#탐색 
def dfs(graph,x,y,temp):
    temp[x][y] = 2    
    for i in range(4): 
        tempX = x + destinationX[i]
        tempY = y + destinationY[i]
        if 0<=tempX<row and 0<=tempY<column and not temp[tempX][tempY] and temp[tempX][tempY]!=1: 
            dfs(graph,tempX,tempY,temp)

maxCount = 0 
for threeWall in wallPickThree:
    count = 0 
    temp = [[0]* column for _ in range(row)]
    #기존 graph 정보 옮겨 담기 
    for i in range(row):
        for j in range(column): 
            temp[i][j] = graph[i][j] 
    #벽 세우기 
    #print("wall pick",threeWall)
    #새로운 벽 
    for x,y in threeWall:
        temp[x][y] = 1
    #print("벽 세워짐",temp) 
    #바이러스 꺼내서 dfs 
    for x,y in virusList:
        dfs(graph,x,y,temp)
    #print("탐색 완료",temp)
    for i in range(row): 
        for j in range(column): 
            if temp[i][j] == 0: 
                count +=1 
    maxCount = max(count,maxCount)

print(maxCount)