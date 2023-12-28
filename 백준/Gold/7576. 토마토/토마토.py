import sys 
input = sys.stdin.readline 
from collections import deque

column, row = map(int,input().rstrip().split())
box = []

q = deque()
for i in range(row):
    box.append(list(map(int,input().rstrip().split())))
    for j in range(column):
        if box[i][j] == 1:
            q.append((i,j))

destinationX = [0,1,0,-1]
destinationY = [1,0,-1,0]

while q: 
    x,y = q.popleft()
    for i in range(4):
        tempX = x + destinationX[i]
        tempY = y + destinationY[i]
        if 0<=tempX<row and 0<=tempY<column and box[tempX][tempY] == 0:
            box[tempX][tempY] = box[x][y] + 1  
            q.append((tempX,tempY))

canFlag = True
answer = 0  
for i in range(row):
    for j in range(column):
        if box[i][j] == 0:
            canFlag = False 
        else:
            answer = max(answer, box[i][j])

if canFlag:
    print(answer-1)
else: 
    print(-1)