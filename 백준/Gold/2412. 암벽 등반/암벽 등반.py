from collections import deque
import sys
input = sys.stdin.readline
INF = int(2e9)

n, T = map(int, input().split())
hole_arr = set()
for _ in range(n) :
    hole_arr.add(tuple(map(int, input().split())))

que = deque()
que.append((0, 0, 0)) # x, y, cost
visited = set() #방문한 노드들 담는 집합
visited.add((0, 0))

#bfs
min_cost = INF
while que :
    x, y, cost = que.popleft()

    #도착했으면 최소값 갱신
    if T <= y :
        min_cost = min(min_cost, cost)
        continue

    #도착 전이면 다음 노드 탐색 - x,y좌표의 차이가 2이하인 범위 내에 노드가 존재하면 탐색
    for hx in range(x-2, x+3) :
        for hy in range(y-2, y+3) :
            if (hx, hy) in hole_arr and (hx, hy) not in visited:
                que.append((hx, hy, cost+1))
                visited.add((hx, hy))


    # #도착 전이면 다음 노드 탐색 - x,y좌표의 차이가 2이하인 노드 탐색
    # for hole in hole_arr :
    #     h_x, h_y = hole
    #     if abs(h_x - x) <= 2 and abs(h_y - y) <= 2 :
    #         if hole not in visited :
    #             que.append((h_x, h_y, cost+1))
    #             visited.add((h_x, h_y))

#목적지에 도착할 수 없는 경우
min_cost = -1 if min_cost == INF else min_cost

print(min_cost)