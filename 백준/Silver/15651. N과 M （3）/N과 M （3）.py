import sys 
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())
res = []
def recur(num):
    if m == num:
        print(' '.join(map(str,res)))
        return
    for i in range(1,n+1): 
        res.append(i)
        recur(num+1)
        res.pop() 

recur(0)