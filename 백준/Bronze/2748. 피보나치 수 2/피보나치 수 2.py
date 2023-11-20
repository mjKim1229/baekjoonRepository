import sys 
input = sys.stdin.readline 
n = int(input().rstrip())
fibo = [0] * (n+1)
fibo[0] = 0 
fibo[1] = 1

def fiboFun(n):
    global fibo
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2] 
    


fiboFun(n)
print(fibo[n])