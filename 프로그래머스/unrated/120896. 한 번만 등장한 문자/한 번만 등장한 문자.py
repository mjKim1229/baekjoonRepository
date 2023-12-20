def solution(s):
    alphaNum = dict()
    oneAlphaList = []
    for alpha in s:
        if alpha in alphaNum: 
            alphaNum[alpha] += 1 
        else: 
            alphaNum[alpha] = 1 
    alphaNum = [x for x in alphaNum if alphaNum[x] ==1]
    alphaNum.sort()
    answer = ''.join(alphaNum)
    return answer
    