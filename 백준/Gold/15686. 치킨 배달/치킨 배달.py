import sys 
input = sys.stdin.readline 
from itertools import combinations

n , limit = map(int,input().rstrip().split())
loc = []
chick = []
house = []
cityChickDistList = []

def calSingleHouse(pick):
    global house
    cityChickDist = 0
    for i,j in house:
        chickDist = (n-1)*(n-1)
        for x,y in pick:
            tempDist = abs(i-x) + abs(j-y)
            chickDist = min(chickDist, tempDist)
        cityChickDist += chickDist
    cityChickDistList.append(cityChickDist)        

for _ in range(n): 
    row = list(map(int,input().rstrip().split()))
    loc.append(row)

#치킨집 위치 탐색 
for i in range(n): 
    for j in range(n): 
        if loc[i][j] == 1:
            house.append((i,j))
        elif loc[i][j] == 2:
            chick.append((i,j))

chickPick = list(combinations(chick,limit))

for pick in chickPick:
    calSingleHouse(pick)

print(min(cityChickDistList))

