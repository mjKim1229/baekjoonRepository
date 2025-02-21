import sys 
input = sys.stdin.readline 
import heapq
N = int(input().rstrip())

queue = []

for _ in range(N):
    array = list(map(int, input().rstrip().split())) 
    for a in array:
        if len(queue) < N: 
            heapq.heappush(queue, a)
        else: 
            if queue[0] < a: 
                heapq.heappop(queue)
                heapq.heappush(queue, a)

print(queue[0])