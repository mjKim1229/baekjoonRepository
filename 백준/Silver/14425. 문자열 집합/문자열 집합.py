import sys 
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

S = set()

for _ in range(n):
    S.add(input().rstrip())

count = 0 
for _ in range(m): 
    nowString = input().rstrip()
    if nowString in S: 
        count +=1

print(count) 
