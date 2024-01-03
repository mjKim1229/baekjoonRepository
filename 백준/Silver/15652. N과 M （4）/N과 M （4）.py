import sys 
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())
#visited = [False] * (n+1)
rs = []
def rec(num): 
    if num == m: 
        print(' '.join(map(str,rs)))
        return
    for i in range(1,n+1):
        if len(rs) ==0 or i>=rs[-1]:
            rs.append(i)
            rec(num+1)
            rs.pop()

rec(0)