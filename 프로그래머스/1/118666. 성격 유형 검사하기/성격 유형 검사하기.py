character = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
def checkScore(a,b):
    global character
    if character[a] > character[b]:
        return a 
    elif character[a] < character[b]:
        return b 
    else: 
        return sorted(a+b)[0]

def solution(survey, choices):
    global character
    answer = ""
    score = [0,1,2,3]
    for i in range(len(survey)): 
        #비동의 
        if choices[i] <=3:
            character[survey[i][0]] += (4-choices[i])
        elif choices[i] >=5:
            character[survey[i][1]] += (choices[i]-4)
    
    print(character)
    answer = answer + checkScore("R","T") + checkScore("C","F") +checkScore("J","M") +checkScore("A","N")
    return answer
    
     