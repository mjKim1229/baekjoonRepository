import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
m = int(input().rstrip())
INF = 1e9

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, input().rstrip().split())
    graph[start][end] = min(graph[start][end], weight) 
    #print("cehck",start, end, weight, graph[start][end])


for i in range(1,n+1):
    for j in range(1,n+1): 
        if i == j: 
            graph[i][j] = 0 


for k in range(1,n+1): 
    for i in range(1,n+1): 
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 

for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n:
            if graph[i][j] == INF: 
                print(0)
            else:
                print(graph[i][j])
        else:
            if graph[i][j] == INF:
                print(0,end=" ")
            else:
                print(graph[i][j],end=" ")