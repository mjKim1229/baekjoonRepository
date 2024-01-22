import sys 
input = sys.stdin.readline 
from collections import defaultdict, deque

n,m = map(int,input().rstrip().split())

jumps = defaultdict(int)
#snakes = defaultdict(int)
for _ in range(n+m):
    index, goto = map(int, input().rstrip().split())
    jumps[index] = goto

INF = int(1e9)
distance = [0] * 101
visited = [False] * 101 

q = deque()
q.append(1)
visited[1] = True 

while q: 
    now = q.popleft()
    if now == 100:
        break 
    for i in range(1,7):
        temp = now + i
        if 1<= temp <=100 and not visited[temp]:
            if temp in jumps.keys():
                temp = jumps[temp]
            
            if not visited[temp]:
                q.append(temp)
                visited[temp] = True 
                distance[temp] = distance[now] + 1 



print(distance[100])
