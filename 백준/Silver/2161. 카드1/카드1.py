from collections import deque 
import sys 
input = sys.stdin.readline

n = int(input().rstrip())

q = deque([x for x in range(1,n+1)])

while q: 
    print(q.popleft(),end=" ")
    q.rotate(-1)