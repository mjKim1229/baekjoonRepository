import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
array.sort()

start, end = 0, N-1 

answer_left, answer_right, min_value = start, end, abs(array[end] + array[start]) 
while start < end: 
    now = array[start] + array[end]
    
    if abs(now) < min_value: 
        answer_left, answer_right = start, end
        min_value = abs(now)
    
    if now > 0: 
        end -= 1 
    elif now < 0: 
        start += 1 
    else: 
        break

print(array[answer_left], array[answer_right]) 