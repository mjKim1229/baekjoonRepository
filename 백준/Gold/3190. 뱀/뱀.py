import sys 
input = sys.stdin.readline 

#0은 빈곳 , s : snake, a : apple 
n = int(input().rstrip())
board = [[0] * n for _ in range(n)]
board[0][0] = 's'
twistDict = dict()
#동 남 서 북 
directionX = [0,1,0,-1]
directionY = [1,0,-1,0]
curDirection = 0 
curHeadLocX , curHeadLocY = 0, 0
curTailLocX, curTailLocY = 0, 0  
sList = []

def changeDirection(count):
    global curDirection
    direction = twistDict[count]
    if direction == "L": 
        curDirection -=1
    elif direction == "D": 
        curDirection +=1  
    
    if curDirection <0: 
        curDirection = 3
    elif curDirection >3: 
        curDirection = 0 
    #print("twist",curDirection)
appleNum = int(input().rstrip())
#사과 입력 
for _ in range(appleNum): 
    i,j = map(int,input().rstrip().split())
    board[i-1][j-1] = 'a'

twistNum = int(input().rstrip())
for _ in range(twistNum):
    time, direction =input().rstrip().split() 
    twistDict[int(time)] = direction


count = 0 
while True:
    if count in twistDict: 
        changeDirection(count)
    curHeadtempX = curHeadLocX + directionX[curDirection]
    curHeadtempY = curHeadLocY + directionY[curDirection]
    #print(curHeadtempX,curHeadtempY,count)
    if 0<= curHeadtempX <n and 0<= curHeadtempY <n and board[curHeadtempX][curHeadtempY] != 's':
        count +=1
        temp = board[curHeadtempX][curHeadtempY]
        board[curHeadtempX][curHeadtempY] = 's'
        sList.append((curHeadLocX,curHeadLocY))
        curHeadLocX, curHeadLocY = curHeadtempX , curHeadtempY
        if temp == 0:
            curTailLocX, curTailLocY = sList.pop(0)
            board[curTailLocX][curTailLocY] = 0
            #print("change tail",curTailLocX,curTailLocY) 
    else:
        #print("out",curHeadtempX,curHeadtempY) 
        break

print(count+1)

