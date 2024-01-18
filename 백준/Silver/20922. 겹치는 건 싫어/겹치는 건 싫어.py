import sys 
from collections import defaultdict
input = sys.stdin.readline 

n, k = map(int, input().rstrip().split())

array = list(  map(int, input().rstrip().split()) )
index = defaultdict(int)

answer = 0 
left, right = 0, 0 

while right < n:
    if index[array[right]] < k: 
        index[array[right]] +=1 
        right +=1 
    else: 
        index[array[left]] -= 1 
        left +=1 
    answer = max(answer,right-left)

print(answer)