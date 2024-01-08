import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
array = list(map(int,input().rstrip().split())) 

target = int(input().rstrip())
start = 1 
end = max(array)

result = 0 
while(start<=end): 
    mid = (start+end)//2
    sum = 0  
    for budget in array:
        if budget > mid: 
            sum += mid
        else: 
            sum += budget
    if sum > target: 
        end = mid -1 
    else: 
        start = mid +1 
        result = mid 

print(result)

    