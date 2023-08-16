import sys 
input = sys.stdin.readline 

#북 , 동 , 남, 서 
destX = [0,1,0,-1]
destY = [-1,0,1,0]

def lookArount(x,y,count):
    for i in range(4):
        tempX = x + destX[i]
        tempY = y + destY[i]
        #범위 안 
        if 0<=tempX<row and 0<=tempY<column:
            #땅  
            if graph[tempX][tempY] == 'X':
                continue
            #바다 
            else:
                count +=1
        #범위 밖  
        else: 
            count +=1
    #print(i,j,count)
    if 3<=count<=4: 
        isIsland[x][y] = False
    else: 
        isIsland[x][y] = True
        checkMinMax(x,y)

row, column = map(int,input().rstrip().split())


minX, maxX , minY, maxY = 10,-1,10,-1
def checkMinMax(x,y):
    global minX, maxX , minY, maxY
    minX = min(x,minX)
    maxX = max(x,maxX)
    minY = min(y,minY)
    maxY = max(y,maxY)

#입력 
graph =[]
for _ in range(row):
    graph.append(list(input().rstrip()))

isIsland = [[False]*(column) for _ in range(row)]

for i in range(row): 
    for j in range(column): 
        if graph[i][j] == 'X':
            count = 0 
            lookArount(i,j,count)

#print(minX, maxX , minY, maxY)

for i in range(minX,maxX+1): 
    for j in range(minY,maxY+1): 
        if isIsland[i][j] == True: 
            print('X',end='')
        else: 
            print('.',end='')
    print()




