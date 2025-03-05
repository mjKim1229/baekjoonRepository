import sys

input = sys.stdin.readline

N, K = map(int, input().split())

stack = []
number = list(input().rstrip())

#앞자리일수록 무조건 크게 만들려고 해야한다. 
#앞에 숫자들을 빼낼 수 있을 만큼 뺴내야한다 
for i in range(N):
    while(K>0 and stack and stack[-1] < number[i]):
        stack.pop()
        K -= 1 
    stack.append(number[i])

print(''.join(stack[:len(stack)-K]))
