import sys
input = sys.stdin.readline 
from collections import deque
from itertools import permutations

totals = list(map(int, input().rstrip().split()))

q = deque()
q.append([0, 0, totals[2]])

visited = list()
visited.append([0, 0, totals[2]])
answer = set()

choices = list(permutations([0, 1, 2], 2))

# 하나가 비거나, 다 차거나 
while q:
    now = q.popleft()
    if now[0] == 0:
        answer.add(now[2])
    for fromIndex, toIndex in choices:
        toIndexLeft = totals[toIndex] - now[toIndex]
        newBottles = now[:]
        # from이 먼저 빔 
        if now[fromIndex] < toIndexLeft:
            newBottles[toIndex] += newBottles[fromIndex]
            newBottles[fromIndex] = 0
        # to가 먼저 참 
        elif now[fromIndex] > toIndexLeft:
            newBottles[toIndex] = totals[toIndex]
            newBottles[fromIndex] -= toIndexLeft
        else:
            newBottles[fromIndex] = 0 
            newBottles[toIndex] = totals[toIndex]
        if newBottles not in visited:
            q.append(newBottles)
            visited.append(newBottles)

answerList = list(answer)
answerList.sort()
print(' '.join(map(str, answerList)))