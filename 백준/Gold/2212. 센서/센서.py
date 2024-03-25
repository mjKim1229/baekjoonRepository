import sys
input = sys.stdin.readline 

censorNum = int(input())
node = int(input())
censorList = list(map(int,input().split()))
censorList.sort()
offsetList = []

for i in range(1,len(censorList)): 
  offsetList.append(censorList[i]-censorList[i-1])

offsetList.sort()
#print(offsetList)
print(sum(offsetList[:censorNum-node]))





  




