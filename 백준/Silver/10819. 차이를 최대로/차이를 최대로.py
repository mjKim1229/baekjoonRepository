import sys
input = sys.stdin.readline 

n = int(input().rstrip())

numList = list(map(int,input().rstrip().split()))
arr = []
visited = [False] * n
max_ans = float('-inf')

def recur(depth):
    global max_ans 
    if depth == n:
        ans = 0 
        for i in range(n-1):
            ans += abs(numList[arr[i]] - numList[arr[i+1]]) 
        max_ans = max(ans, max_ans)
        return 
    for i in range(n):
        if not visited[i]:
            arr.append(i)    
            visited[i] = True 
            recur(depth+1)
            visited[i] = False 
            arr.pop()

recur(0)
print(max_ans)



