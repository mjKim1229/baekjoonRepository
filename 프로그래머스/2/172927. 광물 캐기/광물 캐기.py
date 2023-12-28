def solution(picks, minerals):
    answer = 0 
    min_num = 5 * (sum(picks))
    if min_num < len(minerals):
        minerals = minerals[:min_num]
    
    #최대 50개의 minerals(5개짜리 chunk 10개)
    cnt_min = [[0,0,0] for _ in range(10)]
    for i, mineral in enumerate(minerals):
        chunkNum = i//5
        if mineral == "diamond":
            cnt_min[chunkNum][0] +=1 
        elif mineral == "iron":
            cnt_min[chunkNum][1] +=1 
        elif mineral == "stone": 
            cnt_min[chunkNum][2] +=1 
    
    #diamond, iron, stone 순으로 비싼 광물
    cnt_min.sort(key = lambda x:(-x[0],-x[1],-x[2]))
    
    for mineral in cnt_min: 
        d,i,s = mineral
        for p in range(3):
            if p == 0 and picks[p] >0:
                picks[p] -=1 
                answer += (d+i+s)
                break 
            elif p == 1 and picks[p] >0:
                picks[p] -=1 
                answer += (5*d +i+s)
                break 
            elif p ==2 and picks[p] >0:
                picks[p] -=1 
                answer += (25*d+5*i+s)
                break 
    
    return answer 
                
            