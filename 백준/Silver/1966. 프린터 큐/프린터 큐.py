import sys 
input = sys.stdin.readline 
from collections import deque


for _ in range(int(input().rstrip())):
    n, m = map(int, input().rstrip().split())
    priorityList =list(map(int, input().rstrip().split())) 
    
    queue = deque()
    for i in range(n):
        queue.append((priorityList[i],i))


    count = 1 
    while True: 
        nowPriority, nowIndex = queue.popleft()
        maxPriority = max(priorityList)
        #제일 큰 게 있으면 뒤로 
        if nowPriority < maxPriority:
            queue.append((nowPriority,nowIndex))
        #내가 빠짐 
        else: 
            if nowIndex == m:
                print(count)
                break 
            else:
                priorityList.remove(nowPriority)
                count +=1 

            

    

