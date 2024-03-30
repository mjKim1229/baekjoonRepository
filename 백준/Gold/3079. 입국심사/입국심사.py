import sys

input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())
times = [int(input().rstrip()) for _ in range(N)]

left = 1 
right = min(times) * M 
ans = right 

while left < right: 
    mid = (right + left) // 2 

    cnt = 0 
    for i in times:
        cnt += (mid//i)
    
    if cnt < M: 
        left = mid + 1 
    else: 
        ans = min(ans, mid)
        right = mid 
print(ans)