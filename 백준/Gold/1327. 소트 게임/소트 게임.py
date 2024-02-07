import sys 
input = sys.stdin.readline 
from collections import deque

#n개의 수, k개를 오른쪽으로 뒤집어야함 
n, k = map(int, input().rstrip().split())

array = list(input().rstrip().split()) 
target = sorted(array)

visited = set(''.join(array))

q = deque()
q.append((array,0))

answer = -1 
while q:
    arr, time = q.popleft()
    if arr == target:
        answer = time 
        break 
    # i ~ i+(k-1) // i + k -1 = n-1 // i = n-k까지니까   
    for i in range(n-k+1):
        rarr = arr[i:i+k]
        rarr.reverse()
        arr2 = arr[:i] + rarr + arr[i+k:]
        str2 = ''.join(arr2)
        if str2 not in visited:
            visited.add(str2)
            q.append((arr2,time+1))
    


print(answer)


