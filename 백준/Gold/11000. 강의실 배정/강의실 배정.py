import sys, heapq
input = sys.stdin.readline 

N = int(input().rstrip())
times = []

for _ in range(N):
    start, end = map(int, input().rstrip().split())
    times.append([start, end])

times.sort()

q = []
heapq.heappush(q, times[0][1])
count = 1

for i in range(1, N):
    start, end = times[i]
    if start < q[0]:
        count += 1 
        heapq.heappush(q, end)
    else: 
        heapq.heappop(q)
        heapq.heappush(q, end)

print(count)
    

