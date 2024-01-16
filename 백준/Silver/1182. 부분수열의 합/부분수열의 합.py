import sys 
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())

numList = list(map(int,input().rstrip().split()))

cnt = 0 

def subset_sum(idx,sub_sum):
    global cnt 

    if idx >= n: 
        return 
    
    sub_sum += numList[idx]

    if sub_sum == s: 
        cnt +=1 
    
    subset_sum(idx+1,sub_sum)
    subset_sum(idx+1,sub_sum-numList[idx])

subset_sum(0,0)
print(cnt)