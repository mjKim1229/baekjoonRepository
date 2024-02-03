import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

for _ in range(n):
    array = input().rstrip()
    stack = []
    
    for ch in array:
        if not stack:
            stack.append(ch)
        else: 
            if stack[-1]+ch == '()': 
                stack.pop()
            else: 
                stack.append(ch)
    if stack:
        print("NO")
    else: 
        print("YES")