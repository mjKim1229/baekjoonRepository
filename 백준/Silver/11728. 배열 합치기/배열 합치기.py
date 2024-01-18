import sys 
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())

aArray = list(map(int, input().rstrip().split()))
bArray = list(map(int, input().rstrip().split()))

pointA = 0 
pointB = 0 

result = [0] * (n+m)
resultPoint = 0 
while pointA <n and pointB <m: 
    if aArray[pointA] < bArray[pointB]:
        result[resultPoint] = aArray[pointA]
        pointA += 1 
    else: 
        result[resultPoint] = bArray[pointB]
        pointB += 1 
    resultPoint +=1 

for i in range(pointA,n):
    result[resultPoint] = aArray[i]
    resultPoint += 1 

for i in range(pointB,m):
    result[resultPoint] = bArray[i]
    resultPoint += 1 

print(' '.join(map(str,result))) 