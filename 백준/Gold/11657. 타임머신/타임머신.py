import sys 
input = sys.stdin.readline 
INF = int(1e9)

n, m = map(int, input().split())

edges = []

distance = [INF] * (n+1)

#모든 간선 정보를 입력받기 
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c이다. 
    edges.append((a,b,c))


def bf(start):
    #시작 노드에 대해서 초기화 
    distance[start] = 0 
    #전체 n-1번의 라운드를 반복 
    for i in range(n):
        #매 반복바다 "모든 간선"을 확인 
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n-1: 
                    return True
    return False


negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else: 
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else: 
            print(distance[i])
