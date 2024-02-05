import sys 
input = sys.stdin.readline 

from itertools import combinations

#print(totalList)

while True:
    inputList = list(map(int, input().rstrip().split())) 
    pickNum = inputList[0]
    inputList = inputList[1:]
    if pickNum == 0:
        break

    pickList = list(combinations(inputList,6)) 

    for pick in pickList:
        print(' '.join(map(str, pick)))
    print()
#백트래킹 
# res = []
# def recur(start, count):
#     if count == 6: 
#         print(' '.join(map(str,res))) 
#         return  
#     for i in range(start,pick+1):
#         res.append(lotto[i])
#         recur(i+1,count+1) 
#         res.pop()


# lotto = []
# pick = 0
# while(True):
#     lotto = list(map(int,input().rstrip().split()))
#     if lotto[0] == 0: 
#         break
#     pick = lotto[0] 
#     recur(1,0)
#     print()

# # lotto = list(map(int,input().rstrip().split()))
# # pick = lotto[0]
# # recur(1,0)