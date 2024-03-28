#10000이하 : WEAK 
#10000 초과 100000이하 : Normal 
#100000 초과 1000000이하 : STRONG 
import sys 
input = sys.stdin.readline 

#n : 칭호의 이름 , m: 캐릭터들의 개수 
n, m = map(int, input().rstrip().split())


titles = []
for _ in range(n):
    title, limit = input().rstrip().split()
    titles.append((title,limit))

titles.sort(key=lambda x:int(x[1]))

fights = [int(input().rstrip()) for _ in range(m)]

for fight in fights:
    right = n 
    left = 0 
    result = 0 
    while left <= right:
        mid = (left + right) //2 
        if int(titles[mid][1]) >= fight:
            result = mid 
            right = mid -1 
        else: 
            left = mid +1 
    print(titles[result][0])
