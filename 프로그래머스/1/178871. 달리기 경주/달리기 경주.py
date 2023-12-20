def solution(players, callings):
    #딕셔너리 초기화 
    rankDict = dict()
    for i in range(len(players)): 
        rankDict[players[i]] = i
    for winner in callings:
        winnerRank = rankDict[winner] 
        rankDict[winner] -=1 
        loser = players[winnerRank-1]
        rankDict[loser] +=1 
        players[winnerRank-1], players[winnerRank] = players[winnerRank],players[winnerRank-1]
    return players
        
    