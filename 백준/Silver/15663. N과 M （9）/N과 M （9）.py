import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())
numList = sorted(list(map(int,input().rstrip().split())))
visited = [False] * n 
rs = []

def rec(num, mark):
    #print("check",num,mark)
    if num == m:
        print(' '.join(map(str,rs))) 
        return
    mark = 0 
    for i in range(n):
        if not visited[i] and mark!=numList[i]: 
            rs.append(numList[i])
            visited[i] = True 
            mark = numList[i]
            rec(num+1, mark)
            visited[i]= False 
            rs.pop() 
rec(0,0)
