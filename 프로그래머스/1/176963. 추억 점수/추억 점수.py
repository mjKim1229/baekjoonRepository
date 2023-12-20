def solution(name, yearning, photo):
    scoreDict = dict()
    result = []
    
    for i in range(len(name)): 
        scoreDict[name[i]] = yearning[i]
    
    for singlePhoto in photo:
        score = 0 
        for person in singlePhoto: 
            if person in scoreDict: 
                score += scoreDict[person]
        result.append(score)
    return result