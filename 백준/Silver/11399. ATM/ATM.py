#ATM 1대 사람 N명 

import sys
input = sys.stdin.readline 

n = int(input().rstrip())
time = list(map(int, input().rstrip().split()))

index_time = []
for i in range(n):
    index_time.append((i,time[i]))

index_time.sort(key=lambda x : x[1])

answer = 0 
for i in range(n):
    for j in range(i+1):
        answer += index_time[j][1]

print(answer)