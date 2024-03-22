#운동기구 최대 2개까지 선택 
#헬스장 N개의 운동기구 
#이전에 사용하지 않았던 운동기구 선택 
#되도록이면 2개 
#PT 한번 받을 때 근손실 정도가 M을 넘지 않은 
#M의 최솟값 
import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
muscle_loss = list(map(int, input().rstrip().split()))
muscle_loss.sort()
length = len(muscle_loss)

answer = 0
if length % 2 != 0:
    answer = muscle_loss[length-1]
    length -= 1 
    
for i in range(length//2):
    answer  = max(answer, (muscle_loss[i] + muscle_loss[length-1-i])) 

print(answer)