import sys
input = sys.stdin.readline 
INF = 1e9
n, m = list(map(int, input().rstrip().split()))
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[INF]  * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[0][j] = [board[0][j]] * 3

for i in range(1, n):
    for j in range(m):
        #방향 2 
        if j != 0:
            dp[i][j][2] = board[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])
        #방향 0
        if j != (m - 1):
            dp[i][j][0] = board[i][j] + min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2])
        #방향 1
        dp[i][j][1] = board[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])


min_answer = INF
for j in range(m):          # 마지막 행의 모든 열
    for k in range(3):      # 각 열에서 3방향
        min_answer = min(min_answer, dp[n - 1][j][k])

print(min_answer)