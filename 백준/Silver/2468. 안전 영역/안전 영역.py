from collections import deque

def bfs(start,findDepth,visited):
  queue = deque([start])
  #print(startX,startY)
  while queue:
    startX, startY = queue.popleft()
    visited[startX][startY] = True
    for i in range(4):
      tempX = startX + distanceX[i]
      tempY = startY + distanceY[i]
      #print(tempX,tempY)
      if 0<=tempX<n and 0<=tempY<n and graph[tempX][tempY] >findDepth and not visited[tempX][tempY]:
        visited[tempX][tempY] = True
        queue.append((tempX,tempY))
    
distanceX = [-1,1,0,0]
distanceY = [0,0,-1,1]  

n = int(input())
maxDepth = 0
findDepth = 0 
graph = []



for i in range(n):
  row = list(map(int,input().split()))
  graph.append(row)
  if maxDepth < max(row): 
    maxDepth = max(row)

result = [] 
for findDepth in range(maxDepth):
  count = 0 
  visited = [[False]*n for _ in range(n)]
  for j in range(n):
    for k in range(n):
      if graph[j][k] > findDepth and not visited[j][k]:
        #print(j,k,findDepth,graph[j][k])
        bfs((j,k),findDepth,visited)
        count +=1
  result.append(count)

print(max(result))
  


    


  