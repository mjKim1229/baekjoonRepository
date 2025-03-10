import sys, heapq
input = sys.stdin.readline 

#사람 수, 관계 수 
N, M = map(int, input().rstrip().split())
#사람 
people = [[] for _ in range(N)]

count = 0 
def backtrack(now, visited):
    global count
    if count == 5: 
        print(1)
        sys.exit(0)
    for next in people[now]:
        if not visited[next]:
            visited[next] = True
            count += 1 
            backtrack(next, visited)
            visited[next] = False
            count -= 1 


for _ in range(M):
    a, b = map(int, input().rstrip().split())
    people[a].append(b)
    people[b].append(a)


for start in range(N):
    visited = [False] * (N)
    backtrack(start, visited)

print(0)