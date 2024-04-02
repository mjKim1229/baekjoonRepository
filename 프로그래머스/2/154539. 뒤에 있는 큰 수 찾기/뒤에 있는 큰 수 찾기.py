def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        now = numbers[i]
        while stack and now > numbers[stack[-1]]:
                index = stack.pop()
                answer[index] = now
        stack.append(i)
    
    return answer