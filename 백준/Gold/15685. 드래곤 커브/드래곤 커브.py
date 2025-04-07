import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
board = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def append_direction(direction):
    for i in range(len(direction)-1, -1, -1):
        direction.append(((direction[i] +1) % 4))

    return direction

def turn(x, y, g, d):
    board[x][y] = 1
    
    direction = [d]
    for j in range(g):
        direction = append_direction(direction)
    
    for d in direction:
        x = x + dx[d]
        y = y + dy[d]
        board[x][y] = 1

for _ in range(N):
    y, x, d, g = map(int, input().rstrip().split())
    turn(x, y, g, d)

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
            answer += 1
print(answer)