import sys 
input = sys.stdin.readline 
INF = int(1e9)
C, N = map(int, input().rstrip().split())

city = []
dp = [INF] * (C+100)
dp[0] = 0

for _ in range(N): 
    price, people = map(int, input().rstrip().split())
    city.append((price, people))

for i in range(C+100):  
    for price, people in city:
        if i >= people:
            dp[i] = min(dp[i], dp[i - people] + price)


print(min(dp[C:]))