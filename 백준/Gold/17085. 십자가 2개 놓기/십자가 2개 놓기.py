#[십자가]
#상하좌우 모두 같은 길이의 * 
#[크기] : 중심으로 상하좌우 방향으로 있는 * 개수 
#[넓이]: *가 포함된 개수 

#조건
#2개의 십자가 
# 겹치면 안됨 
# '#'에만 놓을 수 있다. 
#넓이의 곱의 최댓값 
import sys , copy
input = sys.stdin.readline 
from collections import deque
from itertools import combinations


def canSpread(x, y):
    length = 0 
    while True:
        count = 0 
        for i in range(4):
            xx = x + dx[i] * length
            yy = y + dy[i] * length
            if 0<= xx <n and 0<= yy <m and graph[xx][yy] == '#':
              count += 1 
    
        if count == 4:
            canStar.append((x,y,length))
            length += 1 
        else: 
            break

def spread(x,y,length,temp):
    #print(x,y)
    if length == 0:
        if temp[x][y] == True:
            return False
        else: 
            temp[x][y] = True
            return True
    else: 
        for i in range(4):
            xx, yy = x,y
            xx = xx + (dx[i] * length)
            yy = yy + (dy[i] * length)
            if temp[xx][yy] == True:
                return False
            else: 
                temp[xx][yy] = True

        return True

def checkDuplicate(firstStar, secondStar):
    temp = [[False] * m for _ in range(n)]
    fx, fy, fLength = firstStar
    sx, sy, sLength = secondStar
   
    #첫번째 spread 
    for length in range(fLength+1):
        spread(fx,fy,length,temp)
    
    for length in range(sLength+1):
        if spread(sx,sy,length,temp):
            continue 
        else: 
            return None
    
    return ( (fLength*4+1) * (sLength*4+1) )

#격자판 받기 
n, m = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

starLoc = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == '#']
canStar = []

answer = 0 
#가능한 모든 경우의 수 저장 
for x,y in starLoc:
    canSpread(x,y)


for firstStar, secondStar in combinations(canStar,2):
    tempMul = checkDuplicate(firstStar,secondStar) 
    if tempMul != None:
        answer = max(answer,tempMul)

print(answer)

