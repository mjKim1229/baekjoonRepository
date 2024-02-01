#내가 뒤에 있는 주유소의 가격보다 싼 가격 전까지 달림 
import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
distance = list(map(int, input().rstrip().split())) 
cost = list(map(int, input().rstrip().split())) 
distance.append(0)

location = 0 
oilCost = 0
oilLeft = 0  
while True:
    if location == (n-1):
        break 
    #내가 당장 가야할 거리보다 기름이 적다면 
    if oilLeft < distance[location]:
        tempDistance = distance[location]
        for i in range(location+1,n):
            #print("tempDistance",tempDistance)
            if cost[i] >= cost[location]:
                tempDistance += distance[i]
                newLocation = i 
            else: 
                newLocation = i 
                break 
    oilCost += (tempDistance * cost[location])
    #print(location, newLocation, tempDistance, cost[location])
    location = newLocation
    
print(oilCost)