import sys 
input = sys.stdin.readline 

N, L  = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

def rotate(arr):
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[N-j-1][N-1-i] = arr[i][j]
    return ret 

def in_area(index):
    if 0<= index < N: 
        return True
    return False

def check(board):
    bridge = [False for i in range(N)]
    for i in range(N-1):
        if board[i] == board[i+1]:
            continue
    
        if abs(board[i] - board[i+1]) > 1:
            return False
        
        #경사로 놓기 시도 
        if board[i] > board[i+1]:
            temp = board[i+1]

            for j in range(i+1, i+1+L):
                if in_area(j):
                    #같은 높이가 아님 
                    if board[j] != temp:
                        return False
                    #이미 다리가 있으면 
                    if bridge[j] == True:
                        return False
                    bridge[j] = True
                else: 
                    return False
        else: 
            temp = board[i]
            for j in range(i, i-L, -1):
                if in_area(j):
                    if board[j] != temp:
                        return False
                    if bridge[j] == True: 
                        return False
                    bridge[j] = True
                else: 
                    return False
        
    return True

answer = 0 
for board in graph:
    if check(board):
        answer += 1 
    
graph = rotate(graph)

for board in graph:
    if check(board):
        answer += 1 

print(answer)