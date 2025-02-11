import sys 
input = sys.stdin.readline

N, M, L = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

#양 끝 휴게소 있다고 가정 
arr.append(0)
arr.append(L)
arr.sort()

start, end = 1, L

while start <= end: 
    cnt = 0 
    #목표 
    target = (start + end) // 2
    for i in range(1, len(arr)): 
        #간격이 target보다 크면 
        if (arr[i] - arr[i-1]) > target:
            #target을 만족시키는 휴게소를 세운다.
            cnt += (arr[i] - arr[i-1]-1) // target 
    #목표 더 널널하게 
    if cnt > M: 
        start = target + 1
    # 더 좁은 간격 목표로 
    else: 
        end = target - 1 
        answer = target

print(answer)
