import sys 
import heapq
input = sys.stdin.readline 


def dijkstra(start):
    q = []
    distance[start] = 0 
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost: 
                heapq.heappush(q,(cost,i[0]))
                distance[i[0]] = cost     


e, d = map(int,input().rstrip().split())
graph = [[] for _ in range(d+1)]
INF = int(1e9)
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1,1))

for _ in range(e):
    a,b,c = map(int,input().rstrip().split())
    if b > d: 
        continue
    graph[a].append((b,c))


dijkstra(0)
print(distance[d])



