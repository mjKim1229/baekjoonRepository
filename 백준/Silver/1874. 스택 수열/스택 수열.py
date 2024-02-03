import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

stack = []
array = []
for _ in range(n):
    array.append(int(input().rstrip()))

arrayIndex = 0 
inputNum = 1 
answer = []
while True: 
    if arrayIndex == n: 
        break 
    # if inputNum == (n+1):
    #     print(inputNum,"break")
    #     break  
    nextPrint = array[arrayIndex]
    if nextPrint >= inputNum:
        stack.append(inputNum)
        inputNum +=1 
        answer.append('+')
    else: 
        answer.append('-')
        if stack:
            if stack.pop() == nextPrint:
                arrayIndex +=1 
        else: 
            break

if arrayIndex != n: 
    print("NO")
else: 
    for i in answer:
        print(i)