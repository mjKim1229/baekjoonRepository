import sys 
input = sys.stdin.readline 

def reverseWord(word):
    word = list(word)
    str = ""
    wordLength = len(word)
    switchIndex = (wordLength-1)//2
    #print(wordLength,switchIndex) 
    for i in range(switchIndex+1): 
        word[i],word[wordLength-1-i] = word[wordLength-1-i],word[i]
    word = listToString(word)
    return word 

def listToString(list):
    str = ""
    for i in list: 
        str+=i 
    return str

inputWordNum = int(input().rstrip())

result = [[]for _ in range(inputWordNum)]

for i in range(inputWordNum):
    inputWord = input().rstrip().split()
    for splitWord in inputWord: 
        result[i].append(reverseWord(splitWord)) 

#print(result)

for splitWords in result:
    #print(splitWords,len(splitWords))
    for index in range(len(splitWords)):
        #print("see",index,splitWords[index],len(splitWords)-1) 
        if index == (len(splitWords)-1): 
            print(splitWords[index])
        else: 
            print(splitWords[index],end=" ")


    