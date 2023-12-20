def solution(quiz):
    answer = []
    for probs in quiz: 
        isTrue = False 
        prob, result = probs.split("=")
        splits = prob.split()
        if splits[1] == "+": 
            if int(splits[0]) + int(splits[2]) == int(result): 
                isTrue = True 
        elif splits[1] == "-": 
            if int(splits[0]) - int(splits[2]) == int(result): 
                isTrue = True 
        if isTrue: 
            answer.append("O")
        else: 
            answer.append("X")
    return answer