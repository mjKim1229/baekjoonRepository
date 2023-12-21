import sys 
input = sys.stdin.readline 
from collections import defaultdict
haveDict = defaultdict(int)

haveNum = int(input().rstrip())
haveList = list(map(int,input().split())) 

checkNum = input()
checkList = list(map(int,input().split()))

for num in haveList: 
    haveDict[num] +=1 

for num in checkList: 
    print(haveDict[num],end=" ")