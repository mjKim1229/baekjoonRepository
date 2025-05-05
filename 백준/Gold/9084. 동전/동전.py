import sys 
input = sys.stdin.readline 

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    prices = list(map(int, input().rstrip().split()))
    target = int(input().rstrip())
    dp = [0] * (target+1)
    dp[0] = 1

    for p in prices: 
        for t in range(p, target + 1): 
            dp[t] += dp[t - p]

    print(dp[target])