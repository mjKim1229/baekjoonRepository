import sys 
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
array = list(map(int,input().rstrip().split())) 

count = 0
end = 0 
intervalSum =0  
maxSum = -1e9
for start in range(n-m+1):
    while count <m:
        intervalSum += array[end]
        end +=1
        count +=1
    maxSum = max(maxSum, intervalSum)
    intervalSum -= array[start]
    count -=1 

print(maxSum)
    
