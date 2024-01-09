import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
array = list(map(int,input().rstrip().split())) 
m = int(input().rstrip())

end = 0 
intervalSum = 0 
count = 0 

array.sort()

count = 0 
left, right = 0,n-1
while left < right:
    temp = array[left] + array[right]
    if temp == m: 
        count +=1 
        left +=1 
    elif temp <m: 
        left +=1 
    else: 
        right -=1 

print(count)
    
    

         