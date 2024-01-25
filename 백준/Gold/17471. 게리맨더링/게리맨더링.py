import sys 
input = sys.stdin.readline 
from collections import deque
from itertools import combinations

def bfs(split):
    count = 0 
    visited = [False] * (n+1)
    start = split[0]
    visited[start] = True 
    q = deque()
    q.append(start)
    count +=1 
    while q: 
        now = q.popleft()
        for i in graph[now]:
            if i in split and not visited[i]:
                visited[i] = True 
                count +=1 
                q.append(i)

    return count 

n = int(input().rstrip())
populations = [0] * (n+1)
populations[1:] = list(map(int, input().rstrip().split())) 
#print(populations)

graph = [[]]
for _ in range(n):
    inputs = list(map(int,input().rstrip().split()))
    graph.append(inputs[1:])

#print(graph)

visited = [False] * (n+1)

choices = []
indexes = [x for x in range(1,n+1)]
for i in range(1,((n+1)//2) + 1):
    firstSplits = list(combinations(indexes,i)) 
    for firstSplit in firstSplits:
        secondSplit = set(indexes) - set(firstSplit)
        choices.append((firstSplit,tuple(secondSplit)))

answers = []
for firstSplit, secondSplit in choices:
    count = bfs(firstSplit)
    if count == len(firstSplit):
        count = bfs(secondSplit)
        if count == len(secondSplit):
            answers.append(firstSplit)
#print(answers)


totalSum = sum(populations)
answer = int(1e9)
if len(answers) == 0:
    print(-1)
else:
    for firstSplit in answers:
        firstPop = 0 
        for i in firstSplit:
            firstPop += populations[i]
        secondPop =totalSum - firstPop
        #print("final",firstPop,secondPop,totalSum)
        answer = min(answer, abs(firstPop-secondPop))
    print(answer) 