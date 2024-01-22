import sys 
input = sys.stdin.readline 
from collections import deque

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    distance = [ [0] * n for _ in range(n) ] 
    visited = [[0] * n for _ in range(n)]
    
    startX , startY = map(int, input().rstrip().split())
    targetX , targetY = map(int, input().rstrip().split())
    
    visited[startX][startY] = True 
    q = deque()
    q.append((startX, startY))

    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    while q: 
        x,y = q.popleft()
        #print(x,y)
        if x == targetX and y == targetY:
            break 
        for i in range(8):
            tempX = dx[i] + x
            tempY = dy[i] + y 
            if 0<= tempX <n and 0<= tempY <n and not visited[tempX][tempY]:
                distance[tempX][tempY] = distance[x][y] + 1 
                visited[tempX][tempY] = True 
                q.append((tempX,tempY))


    print(distance[targetX][targetY]) 