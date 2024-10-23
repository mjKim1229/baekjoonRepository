import sys 
input = sys.stdin.readline 
from collections import defaultdict
#같은 원소가 K개 이하 최장 연속 부분 수열 

#길이 N , K개 이하 

N, K = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
count_dict = defaultdict(int)

start, end = 0, 0 

#넘어가면 True 
def is_over():
    for value in count_dict.values():
        if value > K:
            return True 
    return False 


left, right = 0, 0 
max_value = 0 
while right < N: 
    if count_dict[array[right]] < K: 
        count_dict[array[right]] += 1 
        right += 1 
    else: 
        count_dict[array[left]] -= 1 
        left += 1 
    max_value = max(right - left, max_value)

print(max_value)










