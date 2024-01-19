import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())
array = list(map(int, input().rstrip().split())) 
array.sort()

visited = [False] * n 
rs = []

#1 7 9 9 
#1
def rec(start):
    if len(rs) == m: 
        print(' '.join(map(str,rs)))
        return
    remember_me = 0 
    for i in range(start,n):
        if not visited[i] and remember_me != array[i]:
            visited[i] = True 
            rs.append(array[i])
            remember_me = array[i]
            rec(i+1)
            visited[i] = False
            rs.pop()
            
rec(0)