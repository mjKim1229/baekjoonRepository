import sys 
input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))


def cut_tree(height):
    cut_sum = 0 
    for tree in trees:
        if tree > height: 
            cut_sum += (tree - height)
    return cut_sum  

start, end = 0, max(trees)
answer = 0 
def binary_search():
    global answer, start, end 
    while start <= end: 
        mid = (start + end) // 2 
        cut_sum = cut_tree(mid)
        if cut_sum >= M: 
            answer = mid 
            start = mid + 1 
        else: 
            end = mid - 1 

binary_search()
print(answer)