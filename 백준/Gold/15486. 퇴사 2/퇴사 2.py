import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
array = []
dp = [0] * (N + 1)
for _ in range(N): 
    T, P = map(int, input().rstrip().split())
    array.append((T,P))

for i in range(N-1, -1, -1):
    T, P = array[i]
    if i + T <= N:
        dp[i] = max(dp[i + T] + P, dp[i+1])
    else: 
        dp[i] = dp[i+1]  

print(max(dp))