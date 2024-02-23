import sys 
input = sys.stdin.readline 

INF = int(1e9) 
v = int(input().rstrip())
e = int(input().rstrip())

graph = [[INF] * (v+1) for _ in range(v+1)]
for i in range(1,v+1):
    for j in range(1,v+1):
        if i == j: 
            graph[i][j] = 0 

for _ in range(e):
    a, b, c = map(int,input().rstrip().split())
    graph[a][b] = min(graph[a][b],c) 

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

for i in range(1,v+1):
    for j in range(1,v+1):
        if graph[i][j] == INF:
            print(0,end=" ")
        else: 
            print(graph[i][j],end=" ")
    print()