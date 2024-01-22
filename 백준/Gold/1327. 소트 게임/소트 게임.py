from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

array = list(input().rstrip().split())
visited = set("".join(array))

target = sorted(array)

q = deque()
q.append([array,0])

answer = -1 

while q: 
    arr, cnt = q.popleft()
    if arr == target: 
        answer = cnt 
        break 
    for i in range(n-k+1):
        rarr = arr[i:i+k]
        rarr.reverse()
        arr2 = arr[:i] + rarr + arr[i+k:]
        str2 = ''.join(arr2)
        if str2 not in visited:
            q.append([arr2,cnt+1])
            visited.add(str2)
        

print(answer)

