import sys 
input = sys.stdin.readline 

n = int(input())

num = list(map(int,input().rstrip().split()))

add, sub , mul, div = map(int,input().rstrip().split())

max_result = - int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global max_result, min_result 
    if n == idx:
        max_result = max(sum, max_result)
        min_result = min(sum, min_result)
    if add: 
        dfs(add-1, sub, mul, div, sum+num[idx],idx+1)
    if sub: 
        dfs(add, sub-1, mul, div, sum-num[idx], idx+1)
    if mul: 
        dfs(add, sub, mul-1, div, sum*num[idx], +idx+1)
    if div: 
        dfs(add, sub, mul, div-1, int(sum/num[idx]), idx+1)
    
dfs(add, sub, mul, div, num[0],1)
print(max_result)
print(min_result)
        


