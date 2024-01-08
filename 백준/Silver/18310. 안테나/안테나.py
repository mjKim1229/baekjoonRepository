import sys 
input = sys.stdin.readline

n = int(input().rstrip())
home = list(map(int,input().rstrip().split()))

home.sort()

print(home[(n-1)//2])