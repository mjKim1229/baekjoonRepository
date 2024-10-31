import sys 
input = sys.stdin.readline 

array = list(input().rstrip()) 

stack = []
answer = 0 
for i in range(len(array)):
    if array[i] == '(':
        stack.append('(') 
    else: 
        stack.pop()
        if array[i-1] == '(':
            answer += len(stack)
        else: 
            answer += 1 

print(answer)




