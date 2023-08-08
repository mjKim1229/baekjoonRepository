import sys 
input = sys.stdin.readline 

number = int(input().rstrip())

paper = [[0 for _ in range(0,101)] for _ in range(101)]

for _ in range(number): 
    x, y = map(int,input().rstrip().split())
    for i in range(x,x+10):
        for j in range(y,y+10): 
            paper[i][j] = 1

count = 0 
for row in paper: 
    count += row.count(1)

print(count)

 

    