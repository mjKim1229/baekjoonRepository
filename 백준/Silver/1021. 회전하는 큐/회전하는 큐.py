#N개의 원소 
#양방향 순환 큐 

#1. 첫번째 원소 뽑 
#2. 왼쪽으로 한 칸 이동 (rotate) 양수 
#3. 오른쪽으로 한칸이동 (rotate) 음수 

#뽑아내려는 원소의 위치  
#2, 3번의 연산의 최솟값 
import sys
input = sys.stdin.readline 
from collections import deque

#N개 원소, 뽑아내려는 개수 M개 
n, m = map(int, input().rstrip().split())

#뽑아내려는 수의 위치 1,2,3 
pickList = list(map(int, input().rstrip().split())) 

q = deque([x for x in range(1,n+1)])

answer = 0 
for pick in pickList:
    while True:
        if q[0] == pick:
            q.popleft()
            break
        else:
            index = q.index(pick)
            if index <= len(q)//2:
                q.rotate(-1)
                answer += 1 
            else: 
                q.rotate(1)
                answer +=1 

print(answer)
