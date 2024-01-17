import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
dp = [1] * n 

for i in range(1,n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp)) 
