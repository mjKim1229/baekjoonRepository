import sys 
input = sys.stdin.readline 
from collections import defaultdict
#교실 N X N 
#학생수 N제곱 
#학생 번호 1 ~ N제곱 
# (1,1) ~ (N,N)
# 학생 - 좋아하는 학생 4명 
# |r1 - r2| + |c1 - c2| = 1

#비어있는 칸 중에 좋아하는 학생이 가장 많은 칸으로 
#1이 여러개라면 비어있는 칸이 많은 칸으로 
# 행 작은칸 => 열 작은칸 

n = int(input().rstrip())
favorites = defaultdict(list)

for _ in range(n*n):
    temp = list(map(int, input().rstrip().split())) 
    favorites[temp[0]] = temp[1:]

graph = [[0] * n for _ in range(n)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def singleSeat(i,j,student,friends):
    favNum = 0 
    blankNum = 0
    for k in range(4):
        xx = i + dx[k]
        yy = j + dy[k]
        if xx<0 or xx>=n or yy<0 or yy>=n:
            continue 
        if graph[xx][yy] in friends:
            favNum +=1
        elif graph[xx][yy] == 0:
            blankNum +=1 
    return (favNum, blankNum, i,j)


for student, friends in favorites.items():
    #print(student,"시작")
    seats = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                seat = singleSeat(i,j,student,friends)
                seats.append(seat)

    seats.sort(key= lambda x: (-x[0],-x[1],x[2],x[3]))
    pick = seats[0]
    #print(student,pick)
    graph[pick[2]][pick[3]] = student


#만족도 구하기 
love = {0:0, 1:1, 2:10, 3:100, 4:1000}
answer = 0 
for i in range(n):
    for j in range(n):
        count = 0 
        student = graph[i][j]
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            if 0<= xx <n and 0<= yy<n: 
                if graph[xx][yy] in favorites[student]:
                    count +=1 
        answer += love[count]
print(answer)
