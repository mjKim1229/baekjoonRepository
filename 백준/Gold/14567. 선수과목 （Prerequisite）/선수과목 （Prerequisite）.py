import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dp = [1] * (n+1)
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)

for i in range(1, n+1):
    for b in arr[i]:
        dp[b] = max(dp[b], dp[i]+1)

print(*dp[1:])
        



