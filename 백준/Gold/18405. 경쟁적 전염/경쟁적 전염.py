import sys 
input = sys.stdin.readline
from collections import deque

#nxn그래프, k초 후 
n, virusNum = map(int, input().rstrip().split())
board = []
initVirus = []

for i in range(n):
    board.append(list(map(int,input().rstrip().split())))
    for j in range(n):
        if board[i][j] != 0:
            initVirus.append((board[i][j],i,j,0))

target_time, target_X, target_Y = map(int,input().rstrip().split())
initVirus.sort()

destinationX = [0,1,0,-1]
destinationY = [1,0,-1,0]

q = deque(initVirus)
while q: 
    virus,x,y,time = q.popleft()
    if time == target_time:
        break
    for i in range(4):
        tempX = x + destinationX[i]
        tempY = y + destinationY[i]
        if 0<=tempX<n and 0<=tempY<n and board[tempX][tempY] == 0:
            board[tempX][tempY] = virus
            q.append((board[tempX][tempY],tempX,tempY,time+1))

print(board[target_X-1][target_Y-1])
