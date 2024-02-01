import sys 
input = sys.stdin.readline 
from collections import deque

n = int(input().rstrip())

list = [x for x in range(1,n+1)]
q = deque(list)

count = n 
while count > 1:
    count -= 1 
    q.popleft()
    q.rotate(-1)

print(q[0])