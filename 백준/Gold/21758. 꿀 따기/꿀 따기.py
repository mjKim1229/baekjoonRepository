import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

ans= 0 

sum = []
sum.append(data[0])

for i in range(1,n):
    sum.append(sum[i-1] + data[i]) 

#맨 왼쪽 꿀통 
for i in range(1,n-1):
    ans = max(ans, sum[n-2] + sum[i-1]-data[i])

#맨 오른쪽 꿀통 
for i in range(1,n-1):
    ans = max(ans, (sum[n-1] - data[0] - data[i]) + (sum[n-1]- sum[i]))

#중앙 꿀통 
for i in range(1,n-1):
    ans = max(ans, sum[n-2]-data[0] + data[i])

print(ans)