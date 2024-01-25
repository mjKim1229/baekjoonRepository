import sys
from collections import deque

dh = [0, 0, 0, 0, -1, 1]
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
def bfs(start, end, distance):
    global dh, dx, dy
    q = deque()
    q.append(start)
    while q: 
        nowH, nowX, nowY = q.popleft()
        if (nowH, nowX, nowY) == end:
            return 
        for i in range(6):
            tempH = nowH + dh[i]
            tempX = nowX + dx[i]
            tempY = nowY + dy[i]
            if 0 <= tempH < h and 0 <= tempX < x and 0 <= tempY < y:
                if distance[tempH][tempX][tempY] == 0 and graph[tempH][tempX][tempY] == '.' or graph[tempH][tempX][tempY] == 'E':
                    distance[tempH][tempX][tempY] = distance[nowH][nowX][nowY] + 1
                    q.append((tempH, tempX, tempY))

while True: 
    h, x, y = map(int, input().rstrip().split())
    if h == 0 and x == 0 and y == 0: 
        break
    graph = []
    for i in range(h):
        oneHeight = []
        for j in range(x):
            row = list(input().rstrip())
            oneHeight.append(row)
            for k in range(y):
                if row[k] == 'S':
                    start = (i,j,k)
                elif row[k] == 'E':
                    end = (i,j,k)
        graph.append(oneHeight)
        input().rstrip()

    distance = [ [ [0] * y for _ in range(x)]  for _ in range(h) ]
    #print(distance)
    bfs(start, end, distance)
    endH , endX , endY = end 
    
    x = distance[endH][endX][endY]
    if distance[endH][endX][endY] == 0: 
        print("Trapped!")
    else: 
        print(f"Escaped in {x} minute(s).")
                    