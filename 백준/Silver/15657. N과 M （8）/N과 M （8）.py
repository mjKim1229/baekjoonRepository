import sys 
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

numList = sorted(list(map(int,input().rstrip().split()))) 
 
rs = []
def rec(num,beforeNum): 
    global rs 
    if num == m:
        print(' '.join(map(str,rs))) 
        return
    for i in range(n):
        if beforeNum <= numList[i]: 
            rs.append(numList[i])
            rec(num+1,numList[i])
            rs.pop()


rec(0,0)