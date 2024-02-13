#지도 N X M 
#지도에 정수 하나씩 써 있음 
#주사위 하나 놓여짐 
#처음 주사위 값 : 모두 0 
#주사위 굴렸을 때 이동한 칸의 값이 0 : 주사위 -> 바닥 
# 0 아니면 : 바닥 -> 주사위 // 바닥 수는 0으로 바뀜 
#바깥으로 못 나감 

import sys 
input = sys.stdin.readline 
#세로, 가로, 주사위 좌표 x, y , 명령 개수  
n, m , x, y, k = map(int,input().rstrip().split())
#명령 
# 1: 동 , 2: 서 , 3: 북, 4 : 남 
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0]
board = []

def turn(dir):
    #위, 뒤, 오, 왼, 앞, 아래 
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c 
    
    elif dir == 2:#서  
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    
    elif dir == 3:#북 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b 
    else: 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e 

for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

comm = list(map(int, input().rstrip().split()))

nx, ny = x,y 
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx <0 or nx >= n or ny<0 or ny>=m: 
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else: 
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0 
    
    print(dice[0])
