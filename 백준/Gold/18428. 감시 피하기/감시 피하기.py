#S: 학생, T: 선생 , O: 벽 
import sys 
input = sys.stdin.readline 
from itertools import combinations
n = int(input().rstrip())
graph = [list(input().rstrip().split()) for _ in range(n)]
teachers = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))


totalNum = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == 'X']
combi = list(combinations(totalNum,3)) 

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for pick in combi:
    avoid = True
    #벽 세우기 
    for x,y in pick:
        graph[x][y] = 'O'
    #선생님 별 탐색 
    for tx, ty in teachers:
        for i in range(4):
            xx , yy = tx, ty 
            while True:
                xx += dx[i]
                yy += dy[i]
                #index out 
                if xx<0 or xx>=n or yy<0 or yy>=n:
                    break 
                #벽 
                if graph[xx][yy] == 'O':
                    break 
                #학생 
                if graph[xx][yy] == 'S':
                    avoid = False
    
    if avoid == True: 
        print("YES")
        exit(0)
    #원래대로 빈칸 복구 
    for x,y in pick:
        graph[x][y] = 'X'
    
print("NO")