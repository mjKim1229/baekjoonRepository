import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())

array = list(map(int,input().rstrip().split()))
array.sort()

rs = []
def rec():
    if len(rs) == m: 
        print(' '.join(map(str,rs)))
        return
    remember_me = 0 
    for i in range(n):
        if remember_me != array[i]:
            rs.append(array[i])
            remember_me = array[i]
            rec()
            rs.pop()

rec()
