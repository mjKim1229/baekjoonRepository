import sys 
input = sys.stdin.readline 
#from itertools import combinations

#수의 개수 
n = int(input().rstrip())
numList = list(map(int, input().rstrip().split())) 
#연산자의 개수 
# + - X % 
add, sub, mul, div = map(int, input().rstrip().split())

#한번에 들어가야할 연산자의 개수는 n-1개 : depth (연산자 더해진 개수)
max_value = -int(1e9)
min_value = int(1e9)
def rec(dsum,depth,index,add,sub,mul,div):
    global max_value, min_value
    if depth == n:
        max_value = max(dsum,max_value)
        min_value = min(dsum,min_value)
        return 
    if add: 
        rec(dsum+ numList[index], depth+1, index+1, add-1, sub, mul, div)
    if sub: 
        rec(dsum- numList[index], depth+1, index+1, add, sub-1, mul, div)
    if mul: 
        rec(dsum * numList[index], depth+1, index+1, add, sub, mul-1, div)
    if div: 
        rec(int(dsum/numList[index]), depth+1, index+1, add, sub, mul, div-1)
    
rec(numList[0],1,1,add, sub, mul, div)
print(max_value)
print(min_value)