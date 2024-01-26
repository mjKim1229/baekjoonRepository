import sys 
input = sys.stdin.readline 

def dfs(s,e,distance):
    #print("check",s,e,distance)
    global answer 
    visited[s] = True 
    for i in graph[s]:
        node = i[0]
        nowDistance = i[1]
        if not visited[node]:
            if node == e:
                answer = distance + nowDistance
            else: 
                dfs(node, e, distance + nowDistance) 


n, m = map(int, input().rstrip().split())

graph = [ [] for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().rstrip().split())    
    graph[a].append((b,d)) 
    graph[b].append((a,d))

for _ in range(m):
    a , b = map(int, input().rstrip().split())
    visited = [False] * (n+1)
    answer = 0 
    #print("called",a,b)
    dfs(a,b,0)
    print(answer)