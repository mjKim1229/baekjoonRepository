import sys
input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())
dots = list(map(int, input().rstrip().split())) 

lines = []
for _ in range(m):
    start, end = map(int, input().rstrip().split())
    lines.append((start,end))

dots.sort()
 
for start, end in lines:
    left, right = 0, n-1 
    if start > dots[right]:
        print(0)
        continue
    while left <= right: 
        mid = (left + right) // 2 
        if start <= dots[mid]:
            startResult = mid 
            right = mid - 1 
        else: 
            left = mid + 1 
    
    left, right = 0, n-1 
    if end < dots[left]: 
        print(0)
        continue
    while left <= right:
        mid = (left + right) //2 
        if end >= dots[mid]:
            endResult = mid
            left = mid + 1 
        else:
            right = mid -1  
            

    #print(startResult,endResult)
    print(endResult-startResult+1)

