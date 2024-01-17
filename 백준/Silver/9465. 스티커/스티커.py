import sys 
input = sys.stdin.readline 


for _ in range(int(input().rstrip())):

    n = int(input().rstrip())
    graph = []
    for _ in range(2):
        row = list(map(int,input().rstrip().split())) 
        graph.append(row)

    dp = [ [0] * n for _ in range(2)]

    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    #열 
    for j in range(1,n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i][j], dp[i+1][j-1] + graph[i][j])
                if 0<= j-2:
                    # print(dp[i+1][j-2])
                    # print(dp[i][j], dp[i+1][j-2] + graph[i][j],graph[i][j] )
                    dp[i][j] = max(dp[i][j], dp[i+1][j-2] + graph[i][j] )
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + graph[i][j])
                if 0<= j-2: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j-2] + graph[i][j] ) 
    
    print(max(dp[0][-1], dp[1][-1]))