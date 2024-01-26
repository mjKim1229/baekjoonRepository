import sys 
input = sys.stdin.readline 

def dfs(s,e,distance):
    #print("check",s,e,distance)
    global answer 
    visited[s] = True 
    for i in range(1,n+1):
        if graph[s][i] > 0 and not visited[i]:
            if i == e:
                answer = distance + graph[s][i]
            else: 
                dfs(i, e, distance + graph[s][i]) 


n, m = map(int, input().rstrip().split())

graph = [ [0] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().rstrip().split())    
    graph[a][b] = d 
    graph[b][a] = d 

for _ in range(m):
    a , b = map(int, input().rstrip().split())
    visited = [False] * (n+1)
    answer = 0 
    #print("called",a,b)
    dfs(a,b,0)
    print(answer)