import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

dp = [0] * (n+1)

for i in range(1,n+1):
    if i ==1 or i ==2 or i==3: 
        dp[i] = i
    else: 
        dp[i] = dp[i-3] + 1 

if i % 2 ==0: 
    print("CY")
else: 
    print("SK")