import sys 
input = sys.stdin.readline 

graph = [[0]*101 for _ in range(101)]

n, m = map(int,input().rstrip().split())

for _ in range(n): 
    firstX, firstY, secondX, secondY = map(int,input().rstrip().split())
    for i in range(firstX,secondX+1): 
        for j in range(firstY,secondY+1): 
            graph[i][j] +=1 

count = 0 
for i in range(101):
    for j in range(101): 
        if graph[i][j] > m: 
            count +=1  

print(count)
