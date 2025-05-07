import sys 
input = sys.stdin.readline 

K, N = map(int, input().rstrip().split())
arr = []
for _ in range(K):
    arr.append(int(input().rstrip())) 

start = 1
end = max(arr)

answer = 0 
while start <= end: 
    mid = (start + end) // 2
    count = 0 
    for lan in arr:
        count += (lan // mid)
    if count >= N:
        answer = mid
        start = mid + 1
    else: 
        end = mid - 1 

print(answer)




