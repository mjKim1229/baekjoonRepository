#맨 위 1장 바닥으로 
#위에서 2번째 바닥 (2장이상)
#제일 밑의 카드 바닥 (2장이상)
#카드 N장 (1~N)
#위에서 부터 순서대로 1~N
#pop한 순서 N ~ 1 

#N
#수열 a 
#ai = x 
#i번째로 카드를 내려놓을 때 x번 기술 씀 
import sys 
input = sys.stdin.readline
from collections import deque
n = int(input().rstrip())
orders = list(map(int, input().rstrip().split()))

final = [x for x in range(1,n+1)]
first = deque()
orders.reverse()

for i in range(n):
    order = orders[i]
    num = final[i]
    if order == 1: 
        first.appendleft(num)
    elif order == 2: 
        first.insert(1,num)
    elif order == 3: 
        first.append(num)

print(*first)