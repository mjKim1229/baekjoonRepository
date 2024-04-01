def solution(sequence, k):
    length = len(sequence)
    left, right = 0, 0
    dSum = 0 
    answerList = []
    while left < length:
        while dSum < k and right < length: 
            dSum += sequence[right]
            right += 1 
            if dSum >=k:
                break 
        if dSum == k: 
            answerList.append((left,right-1,right-left))
        dSum -= sequence[left]
        left += 1 
    answerList.sort(key=lambda x:(x[2],x[0]))
    
    answer = []
    answer.append(answerList[0][0])
    answer.append(answerList[0][1])
    return answer
    