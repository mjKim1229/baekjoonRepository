import sys 
from collections import defaultdict
input = sys.stdin.readline 

n, k = map(int, input().rstrip().split())

array = list(  map(int, input().rstrip().split()) )
index = defaultdict(int)

maxLength = 0 
end = 1
subLength = 1

index[array[0]] +=1 
for start in range(n):
    #print(start,end,subLength)
    while end < n:
        now = array[end]
        if index[now] == k: 
            break 
        end += 1 
        subLength +=1 
        index[now] +=1   
    
    maxLength = max(maxLength, subLength)
    subLength -= 1 
    index[array[start]] -=1 

print(maxLength)