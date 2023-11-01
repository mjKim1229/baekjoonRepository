import sys 
input = sys.stdin.readline 

n , m = map(int,input().rstrip().split())
rs = []
visited = [False] * (n+1)

def recur(num):
    if num == m: 
        print(' '.join(map(str,rs)))
        return 
    for i in range(1,n+1): 
        if not visited[i]:
            visited[i] = True  
            rs.append(i)
            recur(num+1)
            visited[i] = False
            rs.pop()
    

recur(0)