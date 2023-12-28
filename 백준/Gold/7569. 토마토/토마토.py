import sys 
input = sys.stdin.readline 
from collections import deque
q = deque()

column, row, height = map(int,input().rstrip().split())
box = []

for i in range(height):
    tempRow = []
    for j in range(row):
        tempRow.append(list(map(int,input().rstrip().split())))
    box.append(tempRow)

for i in range(height):
    for j in range(row):
        for k in range(column):
            if box[i][j][k] == 1: 
                q.append((i,j,k))

destinationHeight = [0,0,0,0,-1,1]
destinationRow = [0,1,0,-1,0,0]
destinationColumn = [1,0,-1,0,0,0]

while q:
    nowHeight, nowRow, nowColumn = q.popleft()
    for i in range(6):
        tempHeight = nowHeight + destinationHeight[i]
        tempRow = nowRow + destinationRow[i]
        tempColumn = nowColumn + destinationColumn[i]
        if 0<= tempHeight<height and 0<=tempRow<row and 0<=tempColumn<column and box[tempHeight][tempRow][tempColumn] == 0:
            q.append((tempHeight,tempRow,tempColumn))
            box[tempHeight][tempRow][tempColumn] = box[nowHeight][nowRow][nowColumn] + 1 

  
canFlag = True 
answer = 0 
for i in range(height):
    for j in range(row):
        for k in range(column):
            if box[i][j][k] == 0: 
                canFlag = False
            else: 
                answer = max(answer,box[i][j][k])

if canFlag:
    print(answer-1)
else: 
    print(-1)