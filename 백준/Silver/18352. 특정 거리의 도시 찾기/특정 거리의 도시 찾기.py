import sys 
input = sys.stdin.readline 
from collections import deque

def bfs(x):
    visited[x] = True 
    q = deque()
    q.append(x)
    while q: 
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True 
                distance[i] = distance[x] + 1 
                q.append(i)

n, m , k, x = map(int, input().rstrip().split())
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

visited = [False] * (n+1)
distance = [0] * (n+1)
bfs(x)


isNone = True  
for i in range(len(distance)):
    if distance[i] == k: 
        print(i)
        isNone = False 

if isNone:
    print(-1)
