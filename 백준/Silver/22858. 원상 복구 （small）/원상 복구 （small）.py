import sys, copy
input = sys.stdin.readline 

N, K = map(int, input().rstrip().split())
S = list(map(int, input().rstrip().split()))
D = list(map(int, input().rstrip().split()))

before = copy.deepcopy(S)
for _ in range(K):
    new = [0] * N 
    for i in range(N):
        new[D[i]-1] = before[i]
    before = copy.deepcopy(new)
        
print(' '.join(map(str,new)))