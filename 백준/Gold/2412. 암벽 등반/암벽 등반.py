from collections import deque
import sys 
input = sys.stdin.readline 

n, T = map(int, input().rstrip().split())

groove = set()

#홈 데이터 초기화 
for _ in range(n): 
    x, y = map(int, input().rstrip().split())
    groove.add((x,y))

queue = deque()
#x, y , cost 
queue.append((0,0,0))
min_cost = 1e9
visited = set()
visited.add((0,0))

#탐색, 가능한 위치 큐에 넣기 
def checkSurround(x, y, cost):
    for i in range(x-2, x+3): 
        for j in range(y-2, y+3): 
            if (i, j) in groove and (i,j) not in visited: 
                visited.add((i, j))
                queue.append((i, j, cost + 1))


while queue: 
    x, y , cost = queue.popleft()

    #끝났는지 확인, 끝났으면 더 갈 필요가 없음 
    if y >= T:
        min_cost = min(cost, min_cost)
        continue
    
    checkSurround(x, y, cost)

if min_cost == 1e9:
    print(-1)
else: 
    print(min_cost)

