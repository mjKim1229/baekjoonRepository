import sys
input = sys.stdin.readline

# 구간 M
N, M = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

def isValid(target): 
    low = array[0]
    high = array[0]
    d = 1 

    for i in array:
        #범위 내 최댓값 갱신 
        if i > high: 
            high = i 

        if low > i: 
            low = i 

        if high - low > target: 
            #구간 추가 
            d += 1 
            #중단 지점에서부터 새로 시작 
            low = i 
            high = i 

    return M >= d 

start = 0 
end = max(array) - min(array)
answer = end
while start <= end:
    target = (start + end) // 2
    
    if isValid(target): 
        #target을 줄인다 -> 더 많이 쪼개진다 -> M개를 넘어갈수도 있다. 
        end = target - 1
        answer = min(target, answer)
    else:
        start = target + 1
        
print(answer)
