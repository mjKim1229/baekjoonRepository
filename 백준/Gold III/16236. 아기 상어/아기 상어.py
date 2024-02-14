from sys import stdin
from heapq import heappush,heappop
input = stdin.readline

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
q = []

# 2차원 배열에 대한 입력은 끝났으니 상어가 어딨는지 찾아서 넣어주기만 하면 된다.
def init():
    for i in range(n):
        for j in range(n):
            if a[i][j]==9:
                heappush(q,(0,i,j))
                a[i][j]=0
                return

def bfs():
    visited =[ [False] * n for _ in range(n) ]
    size, eat, ans = 2, 0 , 0 
    while q:
        d, x, y = heappop(q)

        #먹는 경우 
        if 0< a[x][y] < size:
            #먹었을 때 답 처리 
            eat += 1 
            a[x][y] = 0 
            ans += d 
            #크기 초기화 하는 경우 
            if eat == size:
                size +=1 
                eat = 0 
            #다시 초기화 
            q.clear()
            d = 0 
            visited =[ [False] * n for _ in range(n) ]
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            dd = d + 1 
            if 0<= xx <n and 0<= yy<n and not visited[xx][yy] and a[xx][yy] <= size: 
                visited[xx][yy] = True 
                heappush(q,(dd,xx,yy))
    print(ans)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
init()
bfs()