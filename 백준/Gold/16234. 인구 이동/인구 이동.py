import sys , math
input = sys.stdin.readline 
import sys
sys.setrecursionlimit(100000)

n , low, high = map(int,input().rstrip().split())
graph = []
for _ in range(n): 
    graph.append(list(map(int,input().rstrip().split())))

visited = [[False]*n for _ in range(n)]

destinationX = [0,1,0,-1]
destinationY = [1,0,-1,0]



def dfs(x,y,unionSet): 
    global destinationX, destinationY, visited, graph
    visited[x][y] = True
    for i in range(4): 
        tempX = x + destinationX[i]
        tempY = y + destinationY[i]
        if 0<=tempX<n and 0<=tempY<n and not visited[tempX][tempY]:
            #print(x,y,tempX,tempY,graph[tempX][tempY],graph[x][y])
            if low <= abs(graph[tempX][tempY]-graph[x][y]) <=high:
                unionSet.add((x,y))
                unionSet.add((tempX,tempY))
                dfs(tempX,tempY,unionSet) 
    #print(unionSet)
    return unionSet

def move():
    global visited, graph
    visited = [[False]*n for _ in range(n)]
    unionList = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                unionSet = set() 
                unionSet = dfs(i,j,unionSet)
                if len(unionSet) >0:
                    unionList.append(list(unionSet))
    return unionList

def changePeople(unionList): 
    global graph 
    for union in unionList:
        sum = 0 
        for x,y in union:
            sum += graph[x][y]
        average = math.floor(sum / len(union)) 
        for x,y in union: 
            graph[x][y] = average 
    
count = 0 
while True: 
    unionList = move()
    #print(unionList)
    if len(unionList) ==0: 
        break 
    else:
        count +=1  
        changePeople(unionList)

print(count)