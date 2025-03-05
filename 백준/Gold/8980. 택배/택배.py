import sys

#마을 수 N, 트럭 용량 C 
N, C = map(int, input().rstrip().split())

#박스 개수 M 
M = int(input().rstrip())

array = []

for _ in range(M):
    start, end, count = map(int, input().rstrip().split())
    array.append((start, end, count))

array.sort(key=lambda x:x[1])

#현재 실은 양 
loads = [0] * (N+1)
answer = 0 
for i in range(M):
    start, end, count = array[i]
    max_loads = 0 
    #구간 중 실어진 최댓값 넣기 
    for j in range(start, end):
        max_loads = max(max_loads, loads[j])
    #들어갈 수 있는 양 
    result = min(count, C-max_loads)
    answer += result 
    for k in range(start, end):
        loads[k] += result

print(answer)