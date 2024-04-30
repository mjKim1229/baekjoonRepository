import math 
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        temp = math.floor(math.sqrt((d**2-i**2)))
        temp2 = (temp//k) + 1 
        answer += temp2
    return answer