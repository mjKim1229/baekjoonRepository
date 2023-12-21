import sys 
input = sys.stdin.readline 
from collections import defaultdict

wordDict = defaultdict(int)

n, lengthLimit = map(int,input().rstrip().split())
for _ in range(n):
    word = input().rstrip()
    if len(word) >= lengthLimit:
        wordDict[word] +=1 

#사전순 정렬 
alphaSortList = sorted(wordDict.items(),key=lambda x:x[0])

#길이 순서대로 정렬 
lengthSortList = sorted(alphaSortList, key=lambda x:len(x[0]),reverse=True)

#자주 나오는 순서대로 정렬 
countSortList = sorted(lengthSortList,key=lambda x:x[1],reverse=True)

for word in countSortList: 
    print(word[0])
