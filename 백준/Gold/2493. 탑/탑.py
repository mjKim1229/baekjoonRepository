import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

stack = []
answer = [0] * (N)

for i in range(N): 
    while stack:    
        #맨위의 실제 값이 크면 answer 초기화 
        if stack[-1][1] > array[i]: 
            answer[i] = stack[-1][0] + 1 
            break
        #뒤에서도 볼필요 없음 
        else: 
            stack.pop()
    
    stack.append((i, array[i]))

print(*answer)