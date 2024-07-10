def solution(players, callings):
    pla_dict = {key: i for i, key in enumerate(players)} 
    
    for backPlayer in callings: 
        backNum = pla_dict[backPlayer]
        pla_dict[backPlayer] -= 1 
        pla_dict[players[backNum-1]] += 1 
        players[backNum], players[backNum-1] = players[backNum-1], players[backNum]
    
    return players