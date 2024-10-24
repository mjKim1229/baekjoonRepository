def solution(sequence, k):
    answer = []
    interval_sum = 0 
    N = len(sequence)
    left, right = 0, 0 
    for left in range(N):
        while right < N and interval_sum < k:
            interval_sum += sequence[right]
            right += 1 
        
        if interval_sum == k: 
            answer.append([left, right-1, right-left+1])
        
        interval_sum -= sequence[left]
    
    answer.sort(key = lambda x : (x[2], x[0]))
    return [answer[0][0], answer[0][1]]           
    