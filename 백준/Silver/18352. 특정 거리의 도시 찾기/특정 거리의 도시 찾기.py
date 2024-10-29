import sys 
input = sys.stdin.readline 

from collections import deque

N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0 
q = deque()
q.append(X)

while q: 
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            q.append(next)
            distance[next] = distance[now] + 1 

if distance.count(K) == 0: 
    print(-1)
else: 
    for i in range(len(distance)):
        if distance[i] == K: 
            print(i)

