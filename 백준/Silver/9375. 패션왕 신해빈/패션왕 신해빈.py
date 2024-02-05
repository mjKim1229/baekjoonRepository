import sys 
input = sys.stdin.readline 
from collections import defaultdict 

#itertools 
for _ in range(int(input().rstrip())):
    closet = defaultdict(int)
    n = int(input().rstrip())
    for _ in range(n):
        a, b =  input().rstrip().split()
        closet[b] += 1 
    

    answer = 1 
    for key in closet.keys():
        answer *= (closet[key] + 1)
    print(answer-1)