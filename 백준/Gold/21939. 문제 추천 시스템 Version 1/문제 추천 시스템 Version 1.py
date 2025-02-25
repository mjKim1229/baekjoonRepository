import sys 
import heapq
input = sys.stdin.readline 
from collections import defaultdict


N = int(input().rstrip())
dict = defaultdict(int)
max_q = []
min_q = []


def recommend(num):
    if num == 1: 
        while dict[-max_q[0][1]] != 0:
            dict[-max_q[0][1]] -= 1 
            heapq.heappop(max_q)
        print(-max_q[0][1])
    else: 
        while dict[min_q[0][1]] != 0: 
            dict[min_q[0][1]] -= 1
            heapq.heappop(min_q)
        print(min_q[0][1])

def add(P, L): 
    heapq.heappush(max_q, (-L, -P))
    heapq.heappush(min_q, (L, P))

def solve(P):
    dict[P] += 1
    
#P 문제 번호 , L 난이도 
#난이도 최대힙 
for _ in range(N): 
    P, L = map(int, input().rstrip().split())
    heapq.heappush(max_q, (-L, -P))
    heapq.heappush(min_q, (L, P))

M = int(input().rstrip())

for _ in range(M): 
    input_list = list(input().rstrip().split())
    command = input_list[0]
    if command == 'recommend':
        recommend(int(input_list[1]))
    elif command == 'add':
        P, L = int(input_list[1]), int(input_list[2])
        add(P, L)
    elif command == 'solved': 
        P = int(input_list[1])
        solve(P)
