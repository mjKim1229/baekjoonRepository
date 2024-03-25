#N개의 회의 진행할 수 있는 최소 회의실 
#시작 - 끝
#회의의 시작 시간은 끝나는 시간보다 항상 작다.
import sys 
input = sys.stdin.readline 
import heapq
n = int(input().rstrip())
time = []
for _ in range(n):
    start, end = map(int, input().rstrip().split())
    time.append((start,end))

time.sort(key= lambda x : (x[0],x[1]))

count = 0 
minList = []

#초기 값 
start, end = time[0]
heapq.heappush(minList,end)
count += 1 


for i in range(1,n):
    start, end = time[i]
    if start >= minList[0]:
        heapq.heappop(minList)
        heapq.heappush(minList,end)
    else: 
        count += 1 
        heapq.heappush(minList, end)
print(count)