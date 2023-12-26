import sys  
input = sys.stdin.readline
from collections import deque

cityNum, roadNum, distance, startCity = map(int,input().rstrip().split())
road = [[] for _ in range(cityNum+1)]
distanceList = [-1] * (cityNum+1)

for _ in range(roadNum): 
    start, end = map(int,input().rstrip().split())
    road[start].append(end)

def bfs(road, startCity):
    queue = deque([startCity])
    distanceList[startCity] = 0 
    while queue: 
        city = queue.popleft()
        #print(city,distanceList[city])
        for i in road[city]: 
            if distanceList[i] == -1: 
                distanceList[i] = distanceList[city] +1 
                queue.append(i)

bfs(road,startCity)

answer = []
for i in range(1,cityNum+1): 
    if distanceList[i] == distance:
        #print(i,distanceList[i]) 
        answer.append(i)
    
if len(answer)==0:
    print(-1) 
else: 
    answer.sort()
    for i in answer: 
        print(i)