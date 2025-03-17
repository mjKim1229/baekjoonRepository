import sys 
input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())

array = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0 

dx = [(0, 1), (0, 1), (0, -1), (0, -1)]
dy = [(1, 0), (-1, 0), (1, 0), (-1, 0)]

def in_area(x1, y1, x2, y2):
    if 0<= x1 < N and 0<= y1 <M and 0<= x2 <N and 0<= y2 <M:
        return True
    return False

def get_score(x, y, x1, y1, x2, y2):
    return array[x][y] * 2 + array[x1][y1] + array[x2][y2]


def dfs(x, y, count):
    global result
    result = max(result, count)

    if x == N: 
        return

    if not visited[x][y]: 
        for i in range(4):
            x1, y1 = x + dx[i][0], y + dx[i][1]
            x2, y2 = x + dy[i][0], y + dy[i][1]

            if in_area(x1, y1, x2, y2):
                if not visited[x1][y1] and not visited[x2][y2]: 
                    visited[x1][y1] = True
                    visited[x2][y2] = True
                    visited[x][y] = True

                    #열 맨 아래까지 도착 -> 행 전환 
                    if y == M-1: 
                        dfs(x+1, 0, count + get_score(x, y, x1, y1, x2, y2))
                    else: 
                        dfs(x, y+1, count + get_score(x, y, x1, y1, x2, y2))

                    visited[x1][y1] = False
                    visited[x2][y2] = False
                    visited[x][y] = False
                
    if y == M-1:
        dfs(x+1, 0, count)
    else: 
        dfs(x, y+1, count)

dfs(0,0,0)
print(result)