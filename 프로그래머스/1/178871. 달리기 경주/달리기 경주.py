def solution(players, callings):
    nameDict, numberDict = {}, {}
    for i in range(len(players)):
        nameDict[players[i]] = i 
        numberDict[i] = players[i]

    for backPlayer in callings: 
        backNum = nameDict[backPlayer]
        frontPlayer = numberDict[backNum-1]
        
        #뒤에 있는 사람 등수 1 감소
        nameDict[backPlayer] -= 1 
        #앞에 있는 사람 등수 1 증가 
        nameDict[frontPlayer] += 1
        
        #앞의 등수 
        numberDict[nameDict[backPlayer]] = backPlayer 
        #뒤의 등수 
        numberDict[nameDict[frontPlayer]] = frontPlayer
    
    answer = []
    for key in numberDict.keys():
        #print(numberDict[key])
        answer.append(numberDict[key])
    
    return answer