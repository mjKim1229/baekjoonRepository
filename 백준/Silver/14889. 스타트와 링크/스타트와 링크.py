import sys 
from itertools import combinations
input = sys.stdin.readline 

n = int(input().rstrip())
array = []
totalSum = 0 
INF = int(1e9)
gap = INF 
for _ in range(n):
    row = list(map(int, input().rstrip().split())) 
    totalSum += sum(row)
    array.append(row)

totalPersonNum = set([x for x in range(n)]) 
refNums = [x for x in range(n)]
#print(totalSum)
choices = list(combinations(refNums,n//2))

for firstTeamChoice in choices: 
    firstTeamScore = 0 
    for x,y in combinations(firstTeamChoice, 2):
        firstTeamScore += (array[x][y] + array[y][x] )
    secondTeamChoice = list(totalPersonNum - set(firstTeamChoice)) 
    secondTeamScore = 0 
    for a,b in combinations(secondTeamChoice,2):
        secondTeamScore += (array[a][b] + array[b][a])
    tempGap = abs(firstTeamScore - secondTeamScore)
    gap = min(tempGap, gap)

print(gap)


    
