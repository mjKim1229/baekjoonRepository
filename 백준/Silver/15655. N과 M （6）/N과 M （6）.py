import sys 
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

numList = sorted(list(map(int,input().rstrip().split()))) 
visited = [False] * n
rs = []

def rec(num, beforeNum): 
    global rs; 
    if num == m:
        print(' '.join(map(str,rs))) 
        return 
    for i in range(n): 
        if not visited[i] and beforeNum < numList[i]:
            rs.append(numList[i])
            visited[i] = True 
            rec(num+1, numList[i])
            rs.pop()
            visited[i] = False 

rec(0,0)
