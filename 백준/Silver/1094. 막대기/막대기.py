import sys 
input = sys.stdin.readline 

X = int(input().rstrip())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0 
for i in range(len(stick)):
    if X >= stick[i]:
        count += 1 
        X -= stick[i]
    if X == 0: 
        break 

print(count)

    
