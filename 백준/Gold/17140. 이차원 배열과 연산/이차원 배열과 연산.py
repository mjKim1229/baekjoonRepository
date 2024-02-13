from collections import Counter 
from functools import reduce

def R(array):
    mx = 0 
    for i in range(len(array)):
        X = Counter(array[i])
        del X[0]
        X = list(X.items())
        X.sort(key=lambda x:(x[1],x[0]))
        if len(X) > 50: X = X[:50]
        array[i] = reduce(lambda x, y : list(x) + list(y), X[1:], list(X[0])) 
        mx = max(mx, len(array[i]))
    for i in range(len(array)):
        if len(array[i]) < mx: 
            array[i].extend([0] * (mx-len(array[i])))
def main():
    r, c, k = map(int, input().rstrip().split())
    r, c = r-1, c-1 

    board = [list(map(int, input().rstrip().split())) for _ in range(3)]
    time = 0 
    if r < len(board) and c < len(board[0]):
        if board[r][c] == k: return time 
    
    while True: 
        if len(board) >= len(board[0]):
            R(board)
        else: 
            board = list(map(list, zip(*board))) 
            R(board)
            board = list(map(list, zip(*board))) 
        time +=1 
        if time > 100: return -1 
        if r < len(board) and c < len(board[0]):
            if board[r][c] == k: return time 

print(main())
            
