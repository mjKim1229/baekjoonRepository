import heapq
def solution(book_time):
    answer = 1
    bookTimeRef = [(
                    int(s[:2])*60 + int(s[3:]),
                    int(e[:2])*60 + int(e[3:])
                   ) for s,e in book_time]
    bookTimeRef.sort()
    heap = []
    for s,e in bookTimeRef: 
        if not heap: 
            heapq.heappush(heap,e+10)
            continue 
        elif heap[0] <= s: 
            heapq.heappop(heap)
        else: 
            answer +=1 
        heapq.heappush(heap,e+10)
        
    
    return answer