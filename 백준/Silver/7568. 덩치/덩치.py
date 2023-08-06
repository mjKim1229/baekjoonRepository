import sys
input = sys.stdin.readline

N = int(input().rstrip())
dungchiList = []
dungchiScore = [1]*N

for _ in range(N):
    a,b = map(int,input().rstrip().split())
    dungchiList.append((a,b))

for i in range(N): 
    for j in range(N):
        #print(dungchiList[i][0],dungchiList[i][1],dungchiList[j][0],dungchiList[j][1]) 
        if dungchiList[i][0] < dungchiList[j][0] and dungchiList[i][1] < dungchiList[j][1]:
            #print(True) 
            dungchiScore[i] +=1

for i in range(N-1):
    print(dungchiScore[i],end=" ")

print(dungchiScore[N-1])
    