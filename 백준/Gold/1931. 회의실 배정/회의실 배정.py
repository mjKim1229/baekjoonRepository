import sys 
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().rstrip().split())
    arr.append((start, end))

arr.sort(key=lambda x: ([x[1], x[0]]))

count = 0 
before = 0 
for start, end in arr:
    if start >= before: 
        count += 1 
        before = end 

print(count)