#크레인 N대 
#1분에 박스를 하나씩 배에 싣는다. 
#모든 크레인 동시에 
import sys 
input = sys.stdin.readline 
import heapq

n = int(input().rstrip())
cranes = list(map(int, input().rstrip().split()))
cranes.sort(reverse=True)
m = int(input().rstrip())
boxes = list(map(int, input().rstrip().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit(0)

count =0 
while boxes:
    for c in cranes:
        #다음 크레인 갖고와야함 : 뒤에 box들도 똑같이 다 처리 못함 
        if boxes and c < boxes[-1]:
            continue
        #지금 크레인으로 무조건 하나 처리 가능함 
        #처리 시 => break 
        for b in boxes:
            if c >= b: 
                boxes.remove(b)
                break
    count += 1

print(count)

   

#https://www.acmicpc.net/board/view/122007

# 2
# 1 2
# 4
# 1 1 2 2

