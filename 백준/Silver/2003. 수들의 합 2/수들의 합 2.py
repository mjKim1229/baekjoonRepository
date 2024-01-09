import sys 
input = sys.stdin.readline

n, m = map(int,input().rstrip().split()) 

array = list(map(int,input().rstrip().split())) 

end = 0 
interval_sum = 0
count = 0   

for start in range(n):
    while interval_sum <m and end <n:
        interval_sum += array[end]
        end +=1 
    if interval_sum == m: 
        count +=1 
    interval_sum -= array[start] 

print(count)

