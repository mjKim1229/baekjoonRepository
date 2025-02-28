import sys
from collections import deque
input = sys.stdin.readline 

start, end = map(int, input().rstrip().split())
MAX = 100001
time = [0] * MAX
def bfs(x, y):
    q = deque()
    if x == 0:
        q.append(1)
    else: 
        q.append(x)
    
    while q: 
        x = q.popleft()
        #잡음 
        if y == x: 
            return time[x]
        
        for nx in (x-1, x+1, 2*x):
            if 0<= nx < MAX and time[nx] == 0:
                if nx == 2*x: 
                    time[nx] = time[x]
                    q.appendleft(nx)
                else: 
                    time[nx] = time[x] + 1
                    q.append(nx)

if start == 0: 
    if end == 0:
        print(0)
    else: 
        print(bfs(start,end) + 1)
else: 
    print(bfs(start, end)) 
