def solution(X, Y):
    answer = ""
    dictX , dictY = dict(), dict()
    
    for x in X: 
        if x in dictX: 
            dictX[x] += 1
        else: 
            dictX[x] = 1 
    for y in Y: 
        if y in dictY: 
            dictY[y] +=1 
        else: 
            dictY[y] =1 
    
    commonNum = set(X) & set(Y)
    if len(commonNum) ==0: 
        return "-1" 
    
    elif "0" in commonNum and len(commonNum)==1: 
        return "0"
    
    for x in commonNum:
        totalNum = min(dictX[x],dictY[x])
        answer += totalNum * x
        
    answer = ''.join(sorted(answer,reverse=True))
    return answer