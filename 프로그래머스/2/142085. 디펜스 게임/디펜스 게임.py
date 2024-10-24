from heapq import heappush, heappop

def solution(n, k, enemy):
    q = []
    
    count = 0 
    enemy_sum = 0 
    for e in enemy:
        heappush(q, -e)
        enemy_sum += e 
        if enemy_sum > n:
            if k == 0: break 
            enemy_sum += heappop(q)
            k -= 1 
        count += 1 
    return count