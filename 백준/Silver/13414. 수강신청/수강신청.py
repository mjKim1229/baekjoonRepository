import sys 
input = sys.stdin.readline 
from collections import defaultdict

limitNum , enterNum = map(int,input().rstrip().split())
waitRankDict = defaultdict(int)

for i in range(enterNum):
    waitRankDict[input().rstrip()] = i 

sortByRank = sorted(waitRankDict.items(), key = lambda x:x[1]) 

for i,value in enumerate(sortByRank): 
    if i >= limitNum:
        break
    else: 
        print(value[0])

