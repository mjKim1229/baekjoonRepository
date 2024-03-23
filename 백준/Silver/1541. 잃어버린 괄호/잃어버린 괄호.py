#양수, +, - , 괄호 
#괄호를 적절히 쳐서 최솟값 
import sys
input = sys.stdin.readline 

array = list(input().rstrip().split('-'))

answer = 0 
for i, exp in enumerate(array):
    forSumList = list(map(int, exp.split('+'))) 
    if i == 0:
        answer += sum(forSumList)
    else: 
        answer -= sum(forSumList)

print(answer)
    