import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

INF = int(1e9)
dp = [INF] * (n+1)


for i in range(3,n+1):
    if i == 3 or i == 5: 
        dp[i] = 1 
    else: 
        if i >=5: 
            dp[i] = min(dp[i-3], dp[i-5]) + 1 
        else: 
            dp[i] = dp[i-3] + 1 

if dp[n] >= INF:
    print(-1)
else: 
    print(dp[n]) 