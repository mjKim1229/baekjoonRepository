import sys 
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().rstrip().split())

q = deque([x for x in range(1,n+1)])


while True:
    if len(q) == 1:
        break 
    if len(q) >= 2: 
        q.append(q.popleft()) 
        if len(q) >= k: 
            for _ in range(k-1):
                q.popleft()
        else: 
            for _ in range(len(q)-1):
                q.popleft()
            

print(q[0])