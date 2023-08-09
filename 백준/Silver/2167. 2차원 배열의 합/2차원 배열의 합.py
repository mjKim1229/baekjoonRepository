import sys 
input = sys.stdin.readline 

rowNumber, columNumber = map(int,input().rstrip().split())
array = []

for _ in range(rowNumber):
    row = list(map(int,input().rstrip().split()))
    array.append(row)
answer = []
targetNumber = int(input())
for _ in range(targetNumber): 
    i,j,x,y = map(int,input().rstrip().split())
    i = i-1
    j = j-1
    x = x-1
    y = y-1
    sum = 0 
    for a in range(i,(x+1)): 
        for b in range(j,(y+1)):
            #print("a","b",a,b)
            sum += array[a][b]
    answer.append(sum) 

for i in answer: 
    print(i)