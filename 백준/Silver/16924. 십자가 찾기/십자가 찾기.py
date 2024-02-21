import sys 
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]

stars = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            stars.append((i,j))

#동 남 서 북 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = []
for x,y in stars:
    #print(x,y,graph)
    length = 1 
    while True: 
        count = 0 
        for i in range(4):
            xx = x + (length * dx[i]) 
            yy = y + (length * dy[i])
            if 0<= xx <n and 0<= yy <m: 
                if graph[xx][yy] == '*' or graph[xx][yy] =='o':
                    count +=1 
        if count == 4: 
            #print("success",x,y)
            graph[x][y] = 'o'
            for i in range(4):
                xx = x + (length * dx[i]) 
                yy = y + (length * dy[i])
                graph[xx][yy] = 'o'
                #print(xx,yy)
            length += 1 
        else: 
            if length > 1: 
                answer.append( (x,y,length-1) )
            break 

#print(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            print(-1)
            exit(0)



print(len(answer)) 
for x,y,s in answer:  
    print(x+1,y+1,s)
