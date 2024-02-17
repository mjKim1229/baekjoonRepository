import sys 
input = sys.stdin.readline
from collections import deque

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    array = list(input().rstrip().split()) 
    q = deque()
    for i, num in enumerate(array):
        if q:
            if q[0] >= num:
                q.appendleft(num)
            else: 
                q.append(num)
        else: 
            q.append(num)
    print(''.join(map(str,q)))