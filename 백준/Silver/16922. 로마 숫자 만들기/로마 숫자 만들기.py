import sys 
input = sys.stdin.readline 
from itertools import combinations_with_replacement
# sys.setrecursionlimit(10**6)
m = int(input().rstrip())


numList = [1, 5, 10, 50]
sumList = [0] * 1001

totalNum = [x for x in range(4)]
numPicks = list(combinations_with_replacement(totalNum,m)) 

for pick in numPicks:
    tempsum = 0 
    for i in range(len(pick)):
        index = pick[i]
        tempsum += numList[index]
    sumList[tempsum] = 1 

print(sum(sumList)) 