import sys 
input = sys.stdin.readline

n = int(input().rstrip())

dp = []
for _ in range(n):
    row = list(map(int,input().rstrip().split())) 
    dp.append(row)

# 2,1 => 1,0 / 1,1 
for i in range(1,n):
    for j in range(i+1):
        #왼쪽 위 
        if j ==0: 
            up_left = 0 
        else: 
            up_left = dp[i-1][j-1]
        #바로 위에서 내려오는 경우 
        if j == i:
            up = 0 
        else: 
            up = dp[i-1][j] 
        dp[i][j] = dp[i][j] + max(up_left,up)

print(max(dp[n-1]))