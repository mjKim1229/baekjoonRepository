def solution(array):
    numCountDict = dict()
    for num in array: 
        if num in numCountDict: 
            numCountDict[num] += 1 
        else: 
            numCountDict[num] = 1 
    
    maxCountList = list(numCountDict.values())
    maxCount = max(maxCountList) 
    if maxCountList.count(maxCount) >1: 
        return -1 
    else: 
        for x in numCountDict: 
            if numCountDict[x] == maxCount: 
                return x
    
    
    