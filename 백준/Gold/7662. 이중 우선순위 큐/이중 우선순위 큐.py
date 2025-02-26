import sys, heapq 
input = sys.stdin.readline 
from collections import defaultdict 

def insert(num):
    num_dict[num] += 1
    heapq.heappush(max_q, -num)
    heapq.heappush(min_q, num)

def pop_max():
    while max_q:
        max_val = -heapq.heappop(max_q)
        if num_dict[max_val] > 0:
            num_dict[max_val] -= 1
            return

def pop_min():
    while min_q:
        min_val = heapq.heappop(min_q)
        if num_dict[min_val] > 0:
            num_dict[min_val] -= 1
            return

def check_max():
    while max_q:
        max_val = -max_q[0]
        if num_dict[max_val] > 0:
            return max_val
        heapq.heappop(max_q)
    return None

def check_min():
    while min_q:
        min_val = min_q[0]
        if num_dict[min_val] > 0:
            return min_val
        heapq.heappop(min_q)
    return None

def cycle():
    global max_q, min_q, num_dict
    k = int(input().rstrip())

    max_q, min_q = [], []
    num_dict = defaultdict(int)

    for _ in range(k):
        command, num = input().rstrip().split()
        num = int(num)

        if command == 'I':
            insert(num)
        elif command == 'D':
            if num == 1:
                pop_max()
            elif num == -1:
                pop_min()

    max_num = check_max()
    min_num = check_min()

    if max_num is None:
        print('EMPTY')
    else:
        print(max_num, min_num)

T = int(input().rstrip())
for _ in range(T):
    cycle()
