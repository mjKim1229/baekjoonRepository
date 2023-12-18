import sys
input = sys.stdin.readline 

n = input().rstrip()
border = int(len(n)/2)

first = sum(map(int,n[:border]))
second = sum(map(int,n[border:]))

if(first==second):
    print("LUCKY")
else: 
    print("READY")