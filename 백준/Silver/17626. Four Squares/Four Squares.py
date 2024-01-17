import sys, math 

n = int(input().rstrip())

INF = int(1e9)
dp = [INF] * (n+1)
dp[0] = 0 
dp[1] = 1 

for i in range(2,n+1):
    maxLimit = int(math.sqrt(i)) 
    for j in range(1,maxLimit+1):
        temp = i - (j*j)
        dp[i] = min(dp[i], dp[temp]+1)

print(dp[n])