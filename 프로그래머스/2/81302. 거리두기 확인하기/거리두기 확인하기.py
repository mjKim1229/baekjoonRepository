from itertools import combinations as C
def solution(places): # 완탐
    
    answer = []
    for case in places:
        temp = []
        for i in case:
            temp.append(list(i))
 
        location = []
        for y in range(5):
            for x in range(5):
                if temp[y][x] == 'P':
                    location.append((x,y)) 
                    
        pair = list(C(location,2)) 
        dist_2 = []
        warn = False
        
        for p1,p2 in pair:
            d = sum(list(map(lambda x,y:abs(x-y), p1,p2))) # 모든 순서쌍 거리 조사
            if d == 1:
                warn = True
                answer.append(0)
                break
            if d == 2:
                a = [p1,p2]
                a.sort()
                dist_2.append(a)
                
        if warn :
            continue
            
        dist_2.sort(key=lambda x:(x[0],x[1]))        
        for p1,p2 in dist_2:
            x1,y1 = p1
            x2,y2 = p2
            if y1==y2 :
                if temp[y1][x1+1] == 'O':
                    warn = True
                    break
            elif x1==x2 :
                if temp[y1+1][x1] == 'O':
                    warn = True
                    break
            elif x1+1==x2 and y1+1==y2 :
                if temp[y1+1][x1] == 'O' or temp[y1][x1+1] == 'O':
                    warn = True
                    break
            elif x1+1==x2 and y1-1==y2 :
                if temp[y1-1][x1] == 'O' or temp[y1][x1+1] == 'O':
                    warn = True
                    break
                    
        if warn : answer.append(0)
        else : answer.append(1)
        
    return answer