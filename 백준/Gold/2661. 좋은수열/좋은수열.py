import sys 
input = sys.stdin.readline 

def check(num):
    length = len(num)
    for idx in range(1,length//2+1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False 
    return True 

def recursive(num):
    if n == len(num):
        print(num)
        exit()
    for i in '123':
        if check(num+str(i)):
            recursive(num+str(i))
        
n = int(input().rstrip())
recursive('1')