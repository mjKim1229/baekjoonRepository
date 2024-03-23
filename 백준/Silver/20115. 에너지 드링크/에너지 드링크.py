import sys 
input = sys.stdin.readline 

n = int(input())
drinkList = list(map(int,input().split())) 
totalAmount = 0 

drinkList.sort(reverse=True)
totalAmount +=  drinkList[0]

remain = sum(drinkList[1:])

if(remain%2==0):
  totalAmount += remain//2
else:
  totalAmount += remain/2

print(totalAmount)
