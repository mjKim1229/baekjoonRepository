import sys 
input = sys.stdin.readline 

n, k = map(int, input().rstrip().split())
start, end = 0, (n//2)

def rip(a): 
    b = n-a
    return (a+1) * (b+1)

can_rip = False
while start <= end: 
    mid = (start + end) // 2
    count = rip(mid)
    if count == k: 
        can_rip = True
        break
    elif count < k:
        start = mid + 1 
    else: 
        end = mid - 1

if can_rip: 
    print("YES")
else: 
    print("NO")
        

