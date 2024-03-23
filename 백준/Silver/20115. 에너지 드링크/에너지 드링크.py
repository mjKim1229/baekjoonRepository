#여러개의 에너지 드링크들을 하나로 
#2개 pick => 한쪽으로 => 절반 흘림 => 남은 드링크 버림 => 하나만 남을 때까지 반복 
import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
array.sort()

answer = array[-1]
for i in range(n-1):
    answer += (array[i]/2)
print(answer)