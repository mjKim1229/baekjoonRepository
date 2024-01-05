import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())
numList = sorted(list(map(int,input().rstrip().split())))

rs = []

def rec(num,beforeNum, mark):
    global visited, rs 
    if num == m:
        print(' '.join(map(str,rs))) 
        return 
    mark = 0 
    for i in range(n):
        if beforeNum <= numList[i] and mark!=numList[i]: 
            rs.append(numList[i])
            mark = numList[i]
            rec(num+1,numList[i], mark)
            rs.pop()

rec(0,0,0)
