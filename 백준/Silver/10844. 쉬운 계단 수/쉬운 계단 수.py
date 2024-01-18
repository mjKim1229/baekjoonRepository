import sys 
input = sys.stdin.readline 
n = int(input().rstrip())

if n == 1: 
    print(9)
else: 
    #행 : 자리수 , 열 : 숫자 
    dp = [ [0] * (10) for _ in range(n+1) ] 

    #1자리수는 모두 1 (1~9)
    for i in range(1,10):
        dp[1][i] = 1 

    for i in range(10):
        dp[2][i] = 2

    dp[2][0] = 1
    #01이 안돼서 1 
    dp[2][1] = 1 
    dp[2][9] = 1 

    for i in range(3,n+1):
        for j in range(10):
            if j == 0: 
                dp[i][j] = dp[i-1][1]
            elif j == 9: 
                dp[i][j] = dp[i-1][8]
            else: 
                dp[i][j] = dp[i-1][j-1]
                dp[i][j] += dp[i-1][j+1]

    #print(dp)
    result = 0 
    for i in range(10):
        result += dp[n][i]   

    print(result %  1000000000)
