import sys 
input = sys.stdin.readline 

# 1 ~ N일 // N+1일 퇴사 //0은 버리는 인덱스 
N = int(input().rstrip())
t = [0]
p = [0]
dp = [0] * (N + 2)
max_value = 0 
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    t.append(x)
    p.append(y)

max_value = 0 
for i in range(N, 0, -1):
    time = i + t[i]
    if time <= (N + 1):
        dp[i] = max(max_value, dp[time] + p[i]) 
        max_value = dp[i]
    else: 
        dp[i] = max_value

print(max_value)