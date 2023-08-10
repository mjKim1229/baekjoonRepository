import sys 
input = sys.stdin.readline 

n = int(input().rstrip())




for k in range(n):
    stack = []
    finish = False
    #print(k)
    ps = input().rstrip()
    for i in ps:
        #print(stack)
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0: 
                print("NO")
                finish = True
                break
            else:
                stack.pop()
    
    if not finish:
        #print("stack",stack)
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
        