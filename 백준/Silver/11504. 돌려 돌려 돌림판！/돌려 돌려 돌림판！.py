import sys 
input = sys.stdin.readline 

testCase = int(input().rstrip())

for i in range(testCase): 
    num , length = map(int,input().rstrip().split())
    startNum = int(''.join(list(input().rstrip().split())))
    finishNum = int(''.join(list(input().rstrip().split())))
    rullet = ''.join(list(input().rstrip().split()))
    count = 0 
    for i in range(num-length+1):
        if startNum <= int(rullet[i:i+length]) <= finishNum: 
            count +=1 
    for i in range(num-length+1,num): 
        tempNum = rullet[i:] + rullet[:length-num+i]
        if startNum <= int(tempNum) <= finishNum: 
            count += 1
    print(count)
