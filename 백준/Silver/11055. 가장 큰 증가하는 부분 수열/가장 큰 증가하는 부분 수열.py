import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
array = list(map(int, input().rstrip().split())) 
dp = [0] * n 

dp = array[:]

for i in range(1,n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i]) 

print(max(dp))
