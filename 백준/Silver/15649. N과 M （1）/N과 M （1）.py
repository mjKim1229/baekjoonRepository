from itertools import permutations
import sys 
input = sys.stdin.readline 

n , m = map(int,input().rstrip().split())

numbers = [i for i in range(1,n+1)]

for numberPick in permutations(numbers,m):
    rs = []
    for num in numberPick:
        rs.append(num)
    print(' '.join(map(str,rs)))
