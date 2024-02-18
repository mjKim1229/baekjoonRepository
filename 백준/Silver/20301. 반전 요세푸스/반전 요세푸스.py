from collections import deque 
import sys 
input = sys.stdin.readline 

#총 n명, k번째 , m명 죽으면 방향 전환 
n, k, m = map(int, input().rstrip().split())

q = deque([x for x in range(1,n+1)])

#-1 : rotate 음수 
direction = -1 
moveCount = 0 
deathCount = 0 
while q:
    if direction < 0:
        if moveCount == (k-1):
            print(q.popleft())
            deathCount += 1 
            moveCount = 0 
        else:
            q.rotate(direction)
            moveCount += 1  
    else: 
        if moveCount == k: 
            print(q.popleft())
            deathCount += 1
            moveCount = 0 
        else: 
            q.rotate(direction)
            moveCount += 1 
    if deathCount == m: 
        direction = -(direction)
        deathCount = 0 