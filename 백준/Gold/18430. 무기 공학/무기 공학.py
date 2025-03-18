import sys 
input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())

array = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0 

#첫번째 
dx = [(0, 1), (0, 1), (0, -1), (0, -1)]
#두번째 
dy = [(1, 0), (-1, 0), (1, 0), (-1, 0)]

def in_area(x, y):
    if 0<= x < N and 0<= y <M: 
        return True
    return False

def get_score(x, y, x1, y1, x2, y2):
    return array[x][y] * 2 + array[x1][y1] + array[x2][y2]

def get_nx(x, y):
    if y == (M-1):
        return x+1, 0 
    else: 
        return x, y + 1

result = 0 
def dfs(x, y, score):
    global result
    result = max(result, score)
    
    if x == N: 
        return 

    nx, ny = get_nx(x, y)
    
    if not visited[x][y]:
        for i in range(4):
            x1, y1 = x + dx[i][0], y + dx[i][1]
            x2, y2 = x + dy[i][0], y + dy[i][1]
            
            #넣고 처리 
            if in_area(x1, y1) and in_area(x2, y2):
                if not visited[x1][y1] and not visited[x2][y2]:
                    visited[x][y] = True
                    visited[x1][y1] = True
                    visited[x2][y2] = True 
                    dfs(nx, ny, score + get_score(x, y, x1, y1, x2, y2))
                    visited[x][y] = False
                    visited[x1][y1] = False
                    visited[x2][y2] = False
            
    #안넣고 처리 
    dfs(nx, ny, score)


dfs(0, 0, 0)

print(result)
