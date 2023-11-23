import heapq, sys 
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

q = []
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m): 
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, (0, start) ) 
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue 
        for i in graph[now]: 
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))  

#print(graph)
dijkstra(start)
for i in range(1,n+1): 
    if distance[i] == INF: 
        print("INF")
    else: 
        print(distance[i])
