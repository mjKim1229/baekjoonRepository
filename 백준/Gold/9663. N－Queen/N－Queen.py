from collections import defaultdict

N = int(input().rstrip())

row = [0] * N 


def promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == (x - i):
            return False

    return True 


count = 0 
def backtrack(x):
    global count
    if x == N: 
        count += 1
        return 
     
    for i in range(N):
        row[x] = i 
        if promising(x):
            backtrack(x + 1)
        

backtrack(0)
print(count)