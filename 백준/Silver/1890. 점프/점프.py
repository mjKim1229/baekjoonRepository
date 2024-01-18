import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

graph = []

for _ in range(n):
    row = list(map(int,input().rstrip().split())) 
    graph.append(row)

dp = [ [0] * n for _ in range(n) ]

dp[0][0] = 1 

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break 
    
        cur = graph[i][j]

        if i + cur < n: 
            dp[i+cur][j] += dp[i][j]
        
        if j + cur < n: 
            dp[i][j+cur] += dp[i][j]
        

        




