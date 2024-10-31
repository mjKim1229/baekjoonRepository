import sys 
input = sys.stdin.readline 

S = input().rstrip()

number_dict = {'1' : 0 , '0' : 0} 

for i in range(len(S)):
    if i == 0: 
        number_dict[S[i]] += 1 
    else: 
        if S[i - 1] != S[i]:
            number_dict[S[i]] += 1 

print(min(number_dict['1'], number_dict['0']))
