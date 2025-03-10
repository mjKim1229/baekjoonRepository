import sys 
from collections import deque
input = sys.stdin.readline 

N, K = map(int, input().rstrip().split())
q = deque([i for i in range(1,N+1)])

answerList = []
while q: 
    for _ in range(K-1):
        q.append(q.popleft())
    answerList.append(str(q.popleft()))

print('<' + ', '.join(answerList)+ ">")


