import sys , heapq 
input = sys.stdin.readline 

n = int(input().rstrip())
heap = []

for _ in range(n):
    num = int(input().rstrip())
    heapq.heappush(heap,num)

for _ in range(n): 
    num = heapq.heappop(heap)
    print(num)