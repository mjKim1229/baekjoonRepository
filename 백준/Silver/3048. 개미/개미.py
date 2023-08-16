import sys 
input = sys.stdin.readline


totalAnt = []

left , right = map(int,input().rstrip().split())

leftAntList = list(input().rstrip())
rightAntList = list(input().rstrip())
time = int(input())

for i in range(left): 
    totalAnt.append((leftAntList[left-i-1],'L'))

for i in range(right): 
    totalAnt.append((rightAntList[i],'R'))


for _ in range(time):
    swapList = [] 
    for i in range(1,len(totalAnt)): 
        if totalAnt[i][1] == 'R' and totalAnt[i-1][1] == 'L':
            swapList.append(i)
    for i in swapList:
        totalAnt[i], totalAnt[i-1] = totalAnt[i-1],totalAnt[i]            


for i in range(len(totalAnt)): 
    print(totalAnt[i][0],end="")