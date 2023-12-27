from itertools import combinations
from collections import deque
import sys 
input = sys.stdin.readline 


n = int(input().rstrip())
graph = []
teacher = []
spaces = []
for i in range(n): 
    graph.append(list(input().rstrip().split()))
    for j in range(n):
        if graph[i][j] == 'T': 
            teacher.append((i,j))
        if graph[i][j] == 'X':
            spaces.append((i,j))

#특정 방향으로 감시를 진행 (True: 학생발견, False: 학생 미발견)
def watch(x,y,direction): 
    #왼쪽 
    if direction == 0: 
        while y >=0:
            if graph[x][y] == "S":
                return True 
            if graph[x][y] == "O":
                return False
            y -=1  
    #오른쪽
    if direction == 1:
        while y<n:
            if graph[x][y] == "S":
                return True 
            if graph[x][y] == "O":
                return False 
            y +=1 
    #위쪽 
    if direction == 2: 
        while x >=0:
            if graph[x][y] == "S":
                return True 
            if graph[x][y] == "O":
                return False 
            x -=1 
    #아래 
    if direction == 3: 
        while x <n: 
            if graph[x][y] == "S":
                return True 
            if graph[x][y] == "O":
                return False 
            x +=1 
    return False

#장애물 설치 이후에, 한명이라도 학생을 찾을 수 있는지 (True: 한명이라도 검사 False: 한명도 못 찾음)
def process():
    for x,y in teacher:
        for i in range(4):
            if watch(x,y,i):
                return True 
    return False 

find = False 
for data in combinations(spaces,3): 
    #벽 세움 
    for x,y in data:
        graph[x][y] = 'O'
    #학생이 한명도 감지 x 
    if not process():
        find = True 
        break 
    #장애물 회수 
    for x,y in data:
        graph[x][y] = 'X'

if find: 
    print("YES")
else: 
    print("NO")