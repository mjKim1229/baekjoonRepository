import sys
input = sys.stdin.readline 

def dfs(x,y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx <n and 0<= yy <m and graph[x][y] == graph[xx][yy]:
            if visited[xx][yy] == 0: 
                visited[xx][yy] = visited[x][y] + 1 
                dfs(xx,yy)
            else: 
                if visited[x][y] - visited[xx][yy] >=3:
                    print("Yes")
                    exit(0)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n) ]
        visited[i][j] = 1 
        dfs(i,j)

print("No")