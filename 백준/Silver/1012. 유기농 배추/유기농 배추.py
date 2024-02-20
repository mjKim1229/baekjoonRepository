from collections import deque

def bfs(startX,startY,graph):
  queue = deque()
  queue.append((startX,startY))
  graph[startX][startY] = -1
  while queue: 
    (nowX, nowY) = queue.popleft()
    #print("now",nowX,nowY)
    for i in range(4):
      #print(i)
      tempX = nowX + distanceX[i]
      tempY = nowY + distanceY[i]
      #print("temp후보",tempX,tempY)
      if 0<=tempX<n and 0<=tempY<m and graph[tempX][tempY] ==1:
        #print("temp",tempX,tempY)
        queue.append((tempX,tempY))
        graph[tempX][tempY] =-1

distanceX = [-1,1,0,0]
distanceY = [0,0,-1,1]

t = int(input())
result = []

for i in range(t):
  #print("test",i)
  m, n, k = map(int,input().split())
  #print(m,n,k)
  graph = [[0]*m for _ in range(n)]
  count = 0
  
  for i in range(k):
    #print(i)
    a,b = map(int,input().split())
    #print(a,b)
    graph[b][a] = 1

  #print(graph)
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        count +=1
        bfs(i,j,graph)
  
  result.append(count)
 
for i in result:
  print(i)