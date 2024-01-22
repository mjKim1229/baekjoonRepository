import sys 
input = sys.stdin.readline 
from collections import deque

#S: 현재 위치 , G: 도착 위치 F:총 층수 
F, S, G, U, D = map(int, input().rstrip().split())

distance = [0] * (F+1)
visited = [False] * (F+1)
q = deque()
q.append(S)
visited[S] = True 
while q: 
    now = q.popleft()
    if now == G: 
        break 
    for next in (now+U, now-D):
        if 1<=next<=F and not visited[next]: 
            q.append(next)
            distance[next] = distance[now] +1
            visited[next] = True

if not visited[G]:
    print("use the stairs")
else: 
    print(distance[G])
