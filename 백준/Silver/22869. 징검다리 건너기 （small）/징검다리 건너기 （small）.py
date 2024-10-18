#N개의 돌 // 1 ~ N 

N, K = map(int, input().rstrip().split())
INF = 1e9
temp = list(map(int, input().rstrip().split()))
rocks = [1e9]
for i in temp:
    rocks.append(i)

dp = [1e9] * (N + 1)
dp[1] = 0

def calculate_strengh(i, j):
    #print(i, j , (j - i) * (1 + abs(rocks[i] - rocks[j])))
    return (j - i) * (1 + abs(rocks[i] - rocks[j]))

# i -> j 
for j in range(2, N + 1):
    for i in range(1, j):
        strength = calculate_strengh(i, j) 
        if strength <= K:
            dp[j] = min(dp[j], dp[i] + strength)

if dp[N] == INF: 
    print("NO")
else: 
    print("YES")


