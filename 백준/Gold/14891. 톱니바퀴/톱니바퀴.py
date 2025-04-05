import sys
input = sys.stdin.readline
from collections import deque

def right(index, d):
    if index > 3: 
        return
    if data[index - 1][2] != data[index][6]:
        right(index + 1, -d)
        data[index].rotate(d)

def left(index, d):
    if index < 0: 
        return
    if data[index][2] != data[index + 1][6]:
        left(index -1, -d)
        data[index].rotate(d)
    

data =  [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input().rstrip())


for _ in range(K):
    index, d = map(int, input().rstrip().split())
    index -= 1 

    left(index - 1, -d)
    right(index + 1, -d)

    data[index].rotate(d)

answer = 0 
for i in range(4):
    if data[i][0] == 1: 
        answer += 2 ** i

print(answer)