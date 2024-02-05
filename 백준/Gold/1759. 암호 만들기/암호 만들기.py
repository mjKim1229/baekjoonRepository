import sys 
input = sys.stdin.readline 
from itertools import combinations

l, c = map(int, input().rstrip().split())
array = list(input().rstrip().split()) 

#1개이상 
voels = []
#2개이상 
notVoels = []
voelRef = ['a','e','i','o','u']

for i in array:
    if i in voelRef:
        voels.append(i)
    else:
        notVoels.append(i)

picks = []
for i in range(1,len(voels)+1):
    notVoelCan = l - i
    if len(notVoels)>= notVoelCan >=2:
        picks.append((i,notVoelCan))

answer = []
for pick in picks:
    voelNum = pick[0]
    notVoelNum = pick[1]
    for tempVoel in combinations(voels,voelNum):
        for tempNotVoel in combinations(notVoels, notVoelNum):
            tempString = ''.join((map(str,tempVoel))) + ''.join(map(str,tempNotVoel))
            answer.append(''.join(sorted(tempString))) 
answer.sort()
for x in answer:
    print(x)
