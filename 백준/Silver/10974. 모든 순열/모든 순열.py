import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
rs = []
visited = [False]*(n+1)

def rec(num):
    if num == n:
        print(' '.join(map(str,rs))) 
        return  
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True 
            rs.append(i)
            rec(num+1)
            visited[i] = False 
            rs.pop()
rec(0)


