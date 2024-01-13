import sys 
input = sys.stdin.readline

n = int(input().rstrip())

array = []
for _ in range(n):
    row = list(map(int,input().rstrip().split())) 
    array.append(row)


dp = [ [0] * n for _ in range(n) ] 

dp[0][0] = array[0][0]

for i in range(1,n):
    for j in range(i+1):
        dy = j -1 
        if 0<= dy <i: 
            dp[i][j] = max(dp[i][j], dp[i-1][dy] + array[i][j])
        dy = j 
        if 0<= dy < i: 
            dp[i][j] = max(dp[i][j], dp[i-1][dy] + array[i][j])



print(max(dp[n-1]))