import sys 
input = sys.stdin.readline 
import heapq

v, e, target = map(int,input().rstrip().split())
result = [0] * (v+1)
INF = int(1e9)

#연결 노드 입력 받기 
#a에서 b까지 거리는 c 
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int,input().rstrip().split())
    graph[a].append((b,c))


def dijkstra(start,distance):
    distance[start] = 0 
    q = []
    heapq.heappush(q,(0,start))
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost: 
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

#각 노드 => target 
for i in range(1,v+1):
    distance = [INF] * (v+1)
    dijkstra(i,distance)
    result[i] += distance[target]

#print(result)

distance = [INF] * (v+1)
dijkstra(target,distance)
for i in range(1,v+1):
    result[i] += distance[i]

print(max(result))