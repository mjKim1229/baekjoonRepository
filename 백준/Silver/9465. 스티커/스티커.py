import sys 
input = sys.stdin.readline 

for _ in range(int(input())):
    N = int(input().rstrip())
    arr = [list(map(int, input().split())) for _ in range(2)]

    #DP 
    dp = [[0] * N for _ in range(2)]

    #0열 고정 
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    if N == 1: 
        print(max(dp[0][0], dp[1][0]))
        continue

    #1열 고정 
    dp[0][1] = arr[0][1] + arr[1][0]
    dp[1][1] = arr[0][0] + arr[1][1]

    if N == 2: 
        print(max(dp[0][1], dp[1][1]))
        continue

    #열 
    for i in range(2, N):
        dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][-1], dp[1][-1]))
