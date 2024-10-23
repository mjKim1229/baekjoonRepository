import sys 
input = sys.stdin.readline 

#블로그 N일, X일 동안의 구간합 
N, X = map(int, input().rstrip().split())

visitors = list(map(int, input().rstrip().split()))

start, end = 0, X - 1 
interval_sum = sum(visitors[start:end+1])
array = [interval_sum]
start += 1 
end += 1 

while end < N:
    interval_sum -= visitors[start-1]
    interval_sum += visitors[end]
    array.append(interval_sum)
    start += 1 
    end += 1 
        
    
    

#print(array)
max_value = max(array)
if max_value == 0: 
    print('SAD')
    exit(0)

print(max_value)
print(array.count(max_value))




