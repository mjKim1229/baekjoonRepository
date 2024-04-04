import heapq 

def solution(n, k, enemy):
    answer, sum_enemy = 0, 0 
    q = []
    for e in enemy: 
        sum_enemy += e 
        heapq.heappush(q, -e) #최대 힙으로 저장 
        if sum_enemy > n: 
            if k == 0: break 
            sum_enemy += heapq.heappop(q)
            k -= 1
        answer += 1 
    return answer 