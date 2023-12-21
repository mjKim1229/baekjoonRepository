def solution(numbers):
    answer = 0 
    total = [False] * 10 
    for number in numbers: 
        if not total[number]: 
            total[number] = True 
    
    print(total)
    for i in range(0,10): 
        if not total[i]: 
            answer += i
    
    return answer