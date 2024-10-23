temp = []
answer = []

def two_pointer(k, sequence):
    left, right = 0, 0 
    N = len(sequence)
    interval_sum = 0 
    for left in range(N):
        while right < N and interval_sum < k:
            interval_sum += sequence[right]
            right += 1 
        
        if interval_sum == k: 
            answer.append((left, right-1, right-left))
        
        interval_sum -= sequence[left]
        left += 1 
    
            
            
            
        
def solution(sequence, k):
    two_pointer(k, sequence)
    answer.sort(key = lambda x : (x[2], x[0]))
    final_answer = []
    final_answer.append(answer[0][0])
    final_answer.append(answer[0][1])
    return final_answer