import sys 
input = sys.stdin.readline 
from collections import defaultdict


n = int(input().rstrip())
favoriteList = defaultdict(list)

for _ in range(n*n):
    temp = list(map(int, input().rstrip().split())) 
    favoriteList[temp[0]] = temp[1:]

board = [ [0] * n for _ in range(n) ] 
#print(favoriteList)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for person in favoriteList.keys():
    locationList = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                favoriteCount = 0 
                blankCount = 0 
                for k in range(4):                
                    tempX = i + dx[k]
                    tempY = j + dy[k]
                    if 0<= tempX <n and 0<= tempY <n:
                        if board[tempX][tempY] in favoriteList[person]: 
                            favoriteCount +=1
                        elif board[tempX][tempY] == 0: 
                            blankCount +=1
                locationList.append((favoriteCount,blankCount,i,j))
    locationList.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]) )
    board[locationList[0][2]][locationList[0][3]] = person 


#만족도 구하기 
answer = 0 
for i in range(n):
    for j in range(n):
        tempFavoriteAnswer = 0 
        for k in range(4):
            tempX = i + dx[k]
            tempY = j + dy[k]
            if 0<=tempX<n and 0<= tempY <n:
                if board[tempX][tempY] in favoriteList[board[i][j]]:
                    tempFavoriteAnswer +=1
        #print(board[i][j],tempFavoriteAnswer)
        if tempFavoriteAnswer > 0:
            answer += (10**(tempFavoriteAnswer-1))

print(answer)
        

