import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dp = [[0] * (K+1) for _ in range(N+1)]

data = []
for _ in range(N):
    weight, value = map(int, input().rstrip().split())
    data.append((weight, value))

for index in range(1, N+1):
    #0부터 시작이니까 index -1 
    weight, value = data[index-1]
    for target in range(1, K+1):
        if weight <= target:
            dp[index][target] = max(dp[index-1][target-weight] + value, dp[index-1][target])
        else: 
            dp[index][target] = dp[index-1][target]

print(dp[N][K])
        

