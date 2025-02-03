import heapq, sys 
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T): 
    answer = 0 
    N = int(input().rstrip())
    files = list(map(int, input().rstrip().split()))
    heapq.heapify(files)
    while len(files) != 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        sum = first + second
        answer += sum
        heapq.heappush(files, sum)
    print(answer)

