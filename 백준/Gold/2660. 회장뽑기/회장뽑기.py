import sys 
input = sys.stdin.readline 
from collections import deque

def bfs(target,visited):
    tempMaxDepth = 0 
    visited[target] = True 
    q = deque()
    q.append((target, 0))
    while q: 
        friend, depth = q.popleft()
        tempMaxDepth = max(depth, tempMaxDepth)
        for i in friends[friend]:
            if not visited[i]:
                visited[i] = True 
                q.append( (i, depth+1) )
    return tempMaxDepth

n = int(input().rstrip())
friends =[ [] for _ in range(n+1) ]
maxDepth = [0] * (n+1)

while True: 
    a, b = map(int, input().rstrip().split())
    if a == -1 and b == -1:
        break 
    friends[a].append(b)
    friends[b].append(a)

for i in range(1,n+1):
    visited = [False] * (n+1)
    tempMaxDepth = bfs(i, visited)
    maxDepth[i] = tempMaxDepth


INF = int(1e9)
minScore = INF 

for i in range(1,n+1):
    if maxDepth[i] != 0: 
        minScore = min(minScore, maxDepth[i])

captainNum = 0 
captains = []
for i in range(1,n+1):
    if maxDepth[i] == minScore:
        captainNum +=1 
        captains.append(i)

print(minScore, captainNum)
print(' '.join(map(str, captains)))

