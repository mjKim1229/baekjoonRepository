import sys
input = sys.stdin.readline 

n, k = map(int,input().rstrip().split())

dp = [[0]*(k+1) for _ in range(n+1)]

value = []
weight = []

for _ in range(n):
    w, v = map(int,input().rstrip().split())
    weight.append(w)
    value.append(v)

for i in range(1,n+1):
    for j in range(1,k+1):
        nowValue = value[i-1]
        nowWeight = weight[i-1]
        if nowWeight > j: 
            dp[i][j] = dp[i-1][j]
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-nowWeight]+nowValue)


print(dp[n][k])