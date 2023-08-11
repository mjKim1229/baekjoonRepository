import sys 
input = sys.stdin.readline

S = input().rstrip()

result = []

for i in range(len(S)): 
    result.append(S[i:]) 

result.sort()

for word in result: 
    print(word)