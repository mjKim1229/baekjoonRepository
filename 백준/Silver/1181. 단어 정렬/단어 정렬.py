import sys 

input = sys.stdin.readline 

n = int(input().rstrip())

words = [[] for _ in range(0,51)]

for _ in range(n): 
    word = input().rstrip()
    wordLength = len(word)
    words[wordLength].append(word)



for wordSet in words: 
    if len(wordSet)>0:
        wordSet.sort()
        tempSet = set(wordSet)
        for resultWord in tempSet:
            print(resultWord)


        



