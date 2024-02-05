import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

for i in range(n-1,0,-1):
    if a[i-1] < a[i]:
        target = i - 1
        break 
else: 
    print(-1)
    exit(0)


for i in range(n-1,0,-1):
    if a[target] < a[i]:
        a[target], a[i] = a[i], a[target]
        a = a[:target+1] + sorted(a[target+1:])
        print(*a)
        break 