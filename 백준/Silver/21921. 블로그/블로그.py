import sys 
input = sys.stdin.readline 

n, x = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

dsum = [0]
temp = 0 
for i in array:
    temp += i 
    dsum.append(temp)

answer = []
for i in range(x,n+1):
    tempSum = dsum[i]-dsum[i-x]
    answer.append(tempSum)

maxNum = max(answer)

if maxNum == 0:
    print("SAD")
else:
    print(maxNum)
    print(answer.count(maxNum))