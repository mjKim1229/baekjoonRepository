import sys 

graph = []
checkGraph = []

for _ in range(5): 
    row = list(map(int,input().rstrip().split())) 
    graph.append(row)

for i in range(5):
    row = [] 
    for j in range(5): 
        row.append(graph[j][i]) 
    graph.append(row)

row = []
for i in range(5): 
    row.append(graph[i][i])
graph.append(row)

row = []
for i in range(5):     
    row.append(graph[4-i][i])
graph.append(row)

visited = [[False]*5 for _ in range(12)]

bingo = 0 
def bingoCheck(num):
    for i in range(12): 
        for j in range(5): 
            if graph[i][j] == num and not visited[i][j]:
                #print(i,j,graph[i][j])
                visited[i][j] = True
                #print(visited[i])
                if False not in visited[i]:
                    global bingo 
                    bingo +=1
                    #print("bingo",visited[i],bingo) 


#빙고 부르기
numCount = 0  
for i in range(5): 
    bingoCheckRow = list(map(int,input().rstrip().split()))
    checkGraph.append(bingoCheckRow)
       
for i in range(5):
    if bingo >= 3:
        break
    for j in range(5):
        bingoCheck(checkGraph[i][j])
        numCount += 1
        #print("num",checkGraph[i][j],numCount,bingo)
        if bingo >= 3:
            break

print(numCount)
           