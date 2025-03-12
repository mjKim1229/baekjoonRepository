import sys 
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
alpha = [False for _ in range(26)]
words = [input().rstrip() for _ in range(N)]
answer = 0 

def check():
    cnt = 0 
    for word in words:
        flag = True
        for c in word: 
            if not alpha[ord(c) - 97]:
                flag = False
                break
        if flag: 
            cnt += 1 
    return cnt 

def backtrack(start, depth):
    global answer 
    if depth == K: 
        answer = max(answer, check())
        return
    
    for i in range(start, 26):
        if not alpha[i]:
            alpha[i] = True
            backtrack(i, depth + 1)
            alpha[i] = False

if K < 5: 
    print(0)
elif K == 26: 
    print(N)
else: 
    for c in ('a', 'c', 'i', 'n', 't'):
        alpha[ord(c) - ord('a')] = True
    
    backtrack(0, 5)

    print(answer)