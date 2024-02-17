import sys 
from collections import deque

input = sys.stdin.readline 

n = int(input().rstrip())
numList = list(map(int, input().rstrip().split())) 

q = deque()
for i in range(1,n+1):
    q.append((i,numList[i-1]))

while q: 
    num, togo = q.popleft()
    print(num,end=" ")
    if togo > 0: 
        q.rotate(-togo+1)
    else: 
        q.rotate(-togo)
