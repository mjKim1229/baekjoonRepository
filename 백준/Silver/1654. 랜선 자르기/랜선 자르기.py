import sys 
input = sys.stdin.readline 

k, n = map(int,input().rstrip().split())
array = []

for _ in range(k): 
    array.append(int(input()))

start = 1 
end = max(array)

result = 0 
while(start<=end):
    mid = (start+end)//2
    piece = 0 
    for num in array: 
        if num >= mid: 
            piece += (num//mid)
    if piece >= n: 
        result = mid 
        start = mid +1 
    else: 
        end = mid -1 

print(result)