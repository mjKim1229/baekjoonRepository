import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
array = list(map(int, input().rstrip().split())) 

small_or_big = [0] * N
for i in range(1, N):
    if array[i-1] > array[i]:
        small_or_big[i] = 1

sum_array = [0]
prefix_sum = 0 
for i in range(N):
    prefix_sum += small_or_big[i]
    sum_array.append(prefix_sum) 

Q = int(input().rstrip())
answer = []
for _ in range(Q):
    start, end = map(int, input().rstrip().split())
    answer.append(sum_array[end] - sum_array[start])

for i in answer:
    print(i)

