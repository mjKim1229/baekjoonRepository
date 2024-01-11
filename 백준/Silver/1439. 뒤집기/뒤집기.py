import sys 
input = sys.stdin.readline 


num = input().rstrip()
countList = [0,0]

first = int(num[0])
countList[first] +=1 
before = first 

for i in range(1,len(num)):
    #print(before,num[i],countList)
    if int(num[i]) != before:
        countList[int(num[i])] +=1 
        before = int(num[i]) 

print(min(countList))