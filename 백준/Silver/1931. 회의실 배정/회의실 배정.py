import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
times = []

for _ in range(N):
    start, end = map(int, input().rstrip().split())
    times.append([start, end])

times.sort(key= lambda x:(x[1], x[0]))

index = 0 
before_end = 0 
count = 0 
while index < N:
    start, end = times[index]
    if start >= before_end: 
        count += 1 
        before_end = end 
    index += 1 

print(count)



