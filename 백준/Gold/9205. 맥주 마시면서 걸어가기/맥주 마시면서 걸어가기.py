import sys 
input = sys.stdin.readline 
from collections import deque

def bfs():
    q = deque()
    q.append((startX,startY))
    while q: 
        x, y = q.popleft()
        distance = abs(endX-x) + abs(endY-y)
        if distance <= 1000:
            print("happy")
            return 
        for i in range(n):
            if not visited[i]:
                newX, newY = stores[i]
                if abs(newX-x) + abs(newY-y) <= 1000:
                    visited[i] = True
                    q.append((newX,newY))
    print("sad")
    return 


#테스트 케이스 
t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    #시작점 
    startX, startY = map(int, input().rstrip().split())
    #편의점 좌표 
    stores = []
    for _ in range(n):
        x,y = map(int, input().rstrip().split())
        stores.append((x,y))

    #편의점 도착 여부 
    visited = [False] * n 
    
    #도착점 
    endX, endY = map(int, input().rstrip().split())
    
    bfs()


