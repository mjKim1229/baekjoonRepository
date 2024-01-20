import sys 
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())

graph = []
#     ←, ↖, ↑,  ↗, →, ↘, ↓, ↙ 1번째 부터 
dx = [0, -1, -1 ,-1, 0, 1 , 1, 1]
dy = [-1,-1, 0,  1 , 1, 1, 0, -1]

#물복사 
copyX = [-1,-1,1,1]
copyY = [-1,1,1,-1]
#1,1번째 => 0,0으로 찾기 
for _ in range(n):
    row = list(map(int, input().rstrip().split()))
    graph.append(row)

cloudList = [(n-2,0), (n-2,1), (n-1,0), (n-1,1)]
disappearList = []
# (N-1, 1), (N-1, 2), (N, 1), (N, 2),
for _ in range(m):
    dir , dist =  map(int, input().rstrip().split())
    disappearList.clear()
    #구름 이동 
    for i in range(len(cloudList)):
        tempX = abs( (cloudList[i][0] + dx[dir-1] * dist ) % n ) 
        tempY = abs( (cloudList[i][1] + dy[dir-1] * dist) % n )  
        #print("goX", (cloudList[i][0] + dx[dir-1] * dist) %n )
        #print("goY", (cloudList[i][1] + dy[dir-1] * dist) %n)
        #print("temp",tempX,tempY)
        graph[tempX][tempY] +=1 
        disappearList.append((tempX,tempY))
        
    #물 복사 
    for i in range(len(disappearList)):
        for j in range(4):
            copyTempX = disappearList[i][0] + copyX[j]
            copyTempY = disappearList[i][1] + copyY[j]
            if 0<= copyTempX <n and 0<= copyTempY <n and graph[copyTempX][copyTempY] > 0: 
                graph[disappearList[i][0]][disappearList[i][1]] += 1
   
    cloudList.clear()
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and (i,j) not in disappearList:
                graph[i][j] -= 2 
                cloudList.append((i,j))
                
    
answer = 0 
for i in range(n):
    for j in range(n):
        answer += graph[i][j]

print(answer)