import sys 
input = sys.stdin.readline

import heapq
n = int(input().rstrip())

heap = []
for _ in range(n): 
    num = int(input().rstrip())
    heapq.heappush(heap,num)

result = 0 
while len(heap) != 1: 
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum = one + two 
    result += sum 
    heapq.heappush(heap,sum)

print(result)
