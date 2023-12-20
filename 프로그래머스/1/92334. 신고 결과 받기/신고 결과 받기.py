def solution(id_list, report, k):
    answer = []
    #신고자 : 신고 받은 사람
    toDeclare = {id:[] for id in id_list}
    #신고 받은 사람 : 신고자 
    fromDeclare = {id:[] for id in id_list}
    #신고 받은 사람 : 신고 횟수 
    declareCount = {id:0 for id in id_list}
    
    for case in report: 
        a,b = case.split()
        if b not in toDeclare[a]:
            toDeclare[a].append(b)
        if a not in fromDeclare[b]:
            fromDeclare[b].append(a)
        
    for a in declareCount: 
        declareCount[a] = len(fromDeclare[a])
    

    for id in id_list:
        count =0 
        #declared는 id가 신고한 사람 리스트 
        for declared in toDeclare[id]:
            #declared가 얼마나 신고당했는지 조회  
            if  declareCount[declared] >= k: 
                count +=1
        answer.append(count)
            
    return answer