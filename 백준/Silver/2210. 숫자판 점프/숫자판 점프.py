import sys 
input = sys.stdin.readline 
import copy

def dfs(x,y,count, rs):
    global answer,numList
    #print(x,y,count,rs)
    rs.append(graph[x][y])
    if count == 6:
        #print("numlist",numList)
        numInString = ''.join(map(str,rs))
        if numInString not in numList:
            answer +=1
            numList.append(numInString) 
        return 
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx <5 and 0<= yy <5:
            dfs(xx,yy,count+1, rs[:]) 

numList = []
graph = []
for _ in range(5):
    row = list(map(int,input().rstrip().split())) 
    graph.append(row)

answer = 0 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(5):
    for j in range(5):
        dfs(i,j,1,[])
#print(numList)
print(answer)