import sys 
input = sys.stdin.readline 


num = input().rstrip()
countList = [0,0]

first = int(num[0])
countList[first] +=1 
before = first 

for i in range(1,len(num)):
    now = int(num[i])
    if now != before:
        countList[now] +=1 
        before = now 

print(min(countList))