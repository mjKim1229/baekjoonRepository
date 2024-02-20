#5 X 5 숫자판 
#숫자 (0~9) 적혀져있음 
#인접 4방향으로 이동 
#5번 이동 
#칸에 있는 숫자 붙임 
import sys 
input = sys.stdin.readline 

graph = [list(map(int, input().rstrip().split())) for _ in range(5)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = set()
answer = 0 
def dfs(x,y,rs,depth):
    global answer 
    if depth == 6: 
        tmp = ''.join(map(str,rs))
        if tmp not in visited:
            visited.add(tmp)
            answer += 1 
        return 
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx<5 and 0<= yy <5:
            rs.append(graph[xx][yy])
            dfs(xx,yy,rs,depth+1)
            rs.pop()

rs = []
for x in range(5):
    for y in range(5):
        rs.append(graph[x][y]) 
        dfs(x,y,rs,1)
        rs.pop()

print(answer)