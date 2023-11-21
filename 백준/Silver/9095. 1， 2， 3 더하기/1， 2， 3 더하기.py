import sys 
input = sys.stdin.readline

case = int(input().rstrip())

for i in range(case):
    result = [0] * 11
    result[0] = 0
    num = int(input().rstrip())
    for j in range(1,num+1):
        for k in range(1,4):
            if j > k:
                #print(j,j-k,result[j-k])
                result[j] += result[j-k]
            elif j == k: 
                result[j] += 1
    print(result[j])
