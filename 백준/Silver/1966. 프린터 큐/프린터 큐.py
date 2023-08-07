from collections import deque
import sys 
input = sys.stdin.readline
result =[]

testCase = int(input().rstrip()) 
for _ in range(testCase):
    queue = []
    number , target = map(int,input().rstrip().split())
    #우선순위 입력 
    priority = list(map(int,input().rstrip().split()))
    #print(priority)
    
    #큐에 삽입 
    for i in range(len(priority)):
        #print(priority[i],i)
        queue.append((priority[i],i))

  
    count = 1 
    
    #조회 
    while True:
        nowPriority,nowIndex = queue.pop(0)
        maxPriority = max(priority)
        #print("뽑은거",nowPriority,nowIndex,maxPriority)
        if nowPriority < maxPriority:
            #print("뒤로")
            queue.append((nowPriority,nowIndex)) 
        else: 
            if nowIndex == target:
                #print("끝")
                #print(count)
                break 
            else:
                #print("그냥 제거")
                priority.remove(maxPriority)
                count +=1 
    result.append(count)

for i in result:
    print(i)

        
    
    