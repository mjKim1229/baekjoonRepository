def solution(rank, attendance):    
    answer = []
    sortedRank = sorted(rank)
    for i in range(len(sortedRank)): 
        index = rank.index(sortedRank[i])
        if attendance[index] == True: 
            answer.append(index)
    
    return answer[0] * 10000 + answer[1] * 100 + answer[2]