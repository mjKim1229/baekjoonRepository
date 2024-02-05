import sys 
input = sys.stdin.readline
from itertools import combinations

n = int(input().rstrip())
graph = []
for _ in range(n):
    row = list(map(int, input().rstrip().split())) 
    graph.append(row)

allNum = [x for x in range(n)]
pickList = list(combinations(allNum, n//2)) 

answer = int(1e9)
for i in range(len(pickList)//2):
    allNumSet = set(allNum)
    firstTeam = list(pickList[i]) 
    firstTeamSum = 0 
    for a,b in combinations(firstTeam,2):
        firstTeamSum += (graph[a][b] + graph[b][a])
    
    secondTeamSum = 0 
    secondTeam = list(allNumSet - set(firstTeam)) 
    for a,b in combinations(secondTeam,2):
        secondTeamSum += (graph[a][b] + graph[b][a])

    answer = min(abs(firstTeamSum-secondTeamSum), answer)

print(answer)
