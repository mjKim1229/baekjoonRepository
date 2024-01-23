import sys 
input = sys.stdin.readline 
from collections import deque

n = int(input().rstrip())
dist = [ [-1] * (n+1) for _ in range(n+1) ]

q = deque()
#화면, 클립보드 
q.append((1,0))
dist[1][0] = 0 
while q: 
    s, c = q.popleft()
    #클립보드 복사 
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] +1  
        q.append((s,s))
    if s + c <= n and dist[s+c][c] == -1: 
        dist[s+c][c] = dist[s][c] + 1 
        q.append((s+c,c))
    if s-1 >=0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] +1 
        q.append((s-1,c))

INF = int(1e9)
answer = INF 
for i in range(n+1):
    if dist[n][i] != -1:
        answer = min(answer, dist[n][i])

print(answer)


