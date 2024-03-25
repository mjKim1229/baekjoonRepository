#1개의 회의실 N개의 회의 
import sys
input = sys.stdin.readline

n = int(input().rstrip())
time = []
for _ in range(n):
    start, end = map(int, input().rstrip().split())
    time.append((start,end))

time.sort(key=lambda x : (x[1], x[0]))

answer = 0 
stopTime = 0 
for start, end in time:
    if start >= stopTime:
        stopTime = end 
        answer += 1 

print(answer)