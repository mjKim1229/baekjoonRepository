import sys 
input = sys.stdin.readline 

# 1 1 2 3 
n, m = map(int,input().rstrip().split())
numList = sorted(set(list(map(int,input().rstrip().split()))))
rs = []

def rec(num):
    if num == m:
        print(' '.join(map(str,rs))) 
        return
    for i in range(n):
        rs.append(numList[i])
        rec(num+1)
        rs.pop() 

rec(0)
