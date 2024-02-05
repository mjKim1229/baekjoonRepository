import sys 
input = sys.stdin.readline 
from itertools import combinations

n, m = map(int, input().rstrip().split())

#백트래킹 
# rs = []
# visited = [False] * (n+1)

# def recur(count, num):
#     if count == m:
#         print(' '.join(map(str,rs))) 
#         return
#     for i in range(n+1):
#         if i > num and not visited[i]:
#             visited[i] = True
#             rs.append(i)
#             recur(count+1,i)
#             visited[i] = False
#             rs.pop() 
             
# recur(0,0)

#itertools 
array = [x for x in range(1,n+1)]

for answer in combinations(array,m):
    for i in answer:
        print(i,end=" ")
    print()