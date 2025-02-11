import sys
input = sys.stdin.readline

# 구간 M
N, M = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

start = 0 
end = max(array) - min(array)
answer = end

def two_pointer(target):
    start, end, count = 0, 0, 0
    while end < len(array):  # end가 array 길이를 넘지 않도록
        gap = max(array[start:end+1]) - min(array[start:end+1])
        if gap <= target:
            end += 1
        else:
            count += 1
            start = end
            end = start
    # 마지막 구간 처리
    if start < len(array):
        count += 1

    return count

while start <= end:
    target = (start + end) // 2
    count = two_pointer(target)

    if count > M:
        start = target + 1
    else:
        end = target - 1
        answer = target

print(answer)
