import sys 
input = sys.stdin.readline 

N = int(input().rstrip())

zarisu = len(str(N)) 
count = 0 

for i in range(1,zarisu):
    count += (9 * 10**(i-1)) *i
#print(count)

zarisuLeft = N - (10**(zarisu-1)) +1
count += (zarisuLeft * zarisu)
print(count)



