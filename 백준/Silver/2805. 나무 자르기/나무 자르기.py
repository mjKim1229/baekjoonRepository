import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())

array = list(map(int,input().rstrip().split()))

start = 0
end = max(array)

result = 0 
while(start<=end):
    mid = (start+end)//2
    sum = 0 
    for tree in array:
        if tree > mid:
            sum += (tree-mid)
    if sum >= m: 
        result = mid
        start = mid + 1
    else: 
        end = mid-1

print(result)