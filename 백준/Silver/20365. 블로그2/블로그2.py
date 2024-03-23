import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().rstrip())
array = input().rstrip()

colorDict = {'R':0, 'B':0}

colorDict[array[0]] += 1 

for i in range(n-1):
    if array[i] != array[i+1]:
        colorDict[array[i+1]] += 1 
        
print(min(colorDict['R'],colorDict['B'])+1) 