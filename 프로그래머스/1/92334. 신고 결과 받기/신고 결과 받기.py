def solution(id_list, report, k):
    answer = []
    #신고자 : 신고 받은 애
    toDeclare = {id:[] for id in id_list}
    fromDeclare = {id:[] for id in id_list}
    declareCount = {id:0 for id in id_list}
    
    for case in report: 
        a,b = case.split()
        if b not in toDeclare[a]:
            toDeclare[a].append(b)
        if a not in fromDeclare[b]:
            fromDeclare[b].append(a)
        
    for a in declareCount: 
        declareCount[a] = len(fromDeclare[a])
    
    toDeclareList = list(toDeclare.items())
    
    for i in toDeclareList: 
        count = 0 
        for j in i[1]:
            if declareCount[j] >= k:
                count += 1
        answer.append(count)
            
    return answer