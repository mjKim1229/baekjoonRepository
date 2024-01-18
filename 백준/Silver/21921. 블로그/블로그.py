import sys 
input = sys.stdin.readline 

n, x = map(int, input().rstrip().split())
array = list( map(int, input().rstrip().split()) )

answer = [] 
sum_value = 0 
dayCount = 0
 
end = 0 
for start in range(n):
    while dayCount < x and end <n: 
        sum_value += array[end]
        dayCount += 1 
        end += 1
    if dayCount == x:
        answer.append(sum_value)
    dayCount -= 1 
    sum_value -= array[start]

maxNumber = max(answer)
if maxNumber == 0: 
    print("SAD")
else: 
    print(maxNumber)
    print(answer.count(maxNumber))
        