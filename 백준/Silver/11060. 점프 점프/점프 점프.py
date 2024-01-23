import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

array = list(map(int, input().rstrip().split())) 
INF = int(1e9)
distacne = [INF] * n 
distacne[0] = 0 

for i in range(n):
    for j in range(1,array[i]+1):
        if i + j < n: 
            distacne[i+j] = min(distacne[i+j], distacne[i]+1)

if distacne[n-1] == INF: 
    print(-1)
else: 
    print(distacne[n-1])