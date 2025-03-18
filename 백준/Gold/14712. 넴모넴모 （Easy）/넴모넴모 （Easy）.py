import sys 
input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())
#M, N이 최대 
array = [[False] * (M + 1) for _ in range(N + 1)]

def check_safe(x, y):
    if not array[x-1][y] or not array[x-1][y-1] or not array[x][y-1]: 
        return True
    return False

def get_n(x, y):
    if y == M: 
        nx = x + 1  
        ny = 1
    else: 
        nx = x 
        ny = y+1 
    
    return nx, ny 

answer = 0 
def dfs(x, y):
    global answer 
    #오른쪽으로 이동 
    if x == (N + 1) and y == 1: 
        answer += 1
        return 
    
    nx, ny = get_n(x,y)

    if check_safe(x,y):    
        array[x][y] = True
        dfs(nx, ny)
        array[x][y] = False
     
    dfs(nx, ny) 
    
dfs(1, 1)
print(answer)