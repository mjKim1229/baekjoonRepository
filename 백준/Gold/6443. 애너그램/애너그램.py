import sys 
input = sys.stdin.readline 


def dfs(rs,visited):
    if len(rs) == len(array):
        print(''.join(map(str,rs)))
        return 
    remember_me = 0 
    for i in range(len(array)):
        if remember_me != array[i] and not visited[i]:
            visited[i] = True 
            remember_me = array[i]
            rs.append(array[i])
            dfs(rs,visited[:]) 
            visited[i] = False
            rs.pop()

for _ in range(int(input().rstrip())):
    array = list(input().rstrip()) 
    array.sort()
    rs = []
    visited = [False] * len(array)
    dfs(rs, visited)
    
    