def solution(keymap, targets):
    answer = []
    keyBoard = dict()
    for key in keymap: 
        for alpha in key: 
            if alpha in keyBoard: 
                keyBoard[alpha] = min(keyBoard[alpha],key.index(alpha)+1) 
            else: 
                keyBoard[alpha] = key.index(alpha) +1  
    
    for target in targets:
        count = 0 
        for alpha in target:
            if alpha not in keyBoard:
                count = -1
                break
            else: 
                count += keyBoard[alpha]
        answer.append(count)
            
    return answer