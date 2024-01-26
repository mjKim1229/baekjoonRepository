import sys 
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())
INF = int(1e9)
distance = [ [INF] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    distance[a][b] = 1 

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j: 
            distance[i][j] = 0 


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j] ) 

answer = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i!= j and distance[i][j] != INF:
            answer[i] += 1 
            answer[j] += 1 

print(answer.count(n-1))