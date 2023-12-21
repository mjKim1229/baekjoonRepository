import sys 
input = sys.stdin.readline 
from collections import defaultdict

for _ in range(int(input())):
    clothNum = int(input())
    if clothNum == 0: 
        print(0)
    else:
        clothDict = defaultdict(int) 
        for _ in range(clothNum):
            answer = 1  
            clothe , kind = input().rstrip().split()
            clothDict[kind] += 1
        for value in clothDict.values(): 
            answer *= (value+1)
        print(answer -1) 
    