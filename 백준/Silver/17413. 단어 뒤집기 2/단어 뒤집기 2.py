import sys 
input = sys.stdin.readline 

reversedWords = []
def reverseWord(words):
    for word in words:
        reversedWords.append(word[::-1])

S = input()
words = []

bracketNumber = S.count("<")
if bracketNumber ==0:
    #print("noTag")
    words = list(S.split())
    reverseWord(words)
    answer = " ".join(reversedWords)
    #print(answer)
else:
    #print("tag")
    #first 
    endIndex=S.index("<")
    tempString = S[0:endIndex]
    S = S[endIndex:]
    words = list(tempString.split())
    reverseWord(words)
    for i in range(bracketNumber-1):
        reversedWords.append(S[S.index("<"):S.index(">")+1])
        S = S[1:]
        startIndex = S.index(">")
        endIndex = S.index("<")
        tempString = S[startIndex+1:endIndex]
        S = S[endIndex:]
        words = list(tempString.split())
        reverseWord(words)
    #last
    startIndex = S.index("<")
    endIndex = S.index(">")
    reversedWords.append(S[startIndex:endIndex+1])
    tempString = S[endIndex+1:]
    words = list(tempString.split())
    reverseWord(words)


#print(reversedWords)

for i in range(len(reversedWords)-1): 
    if reversedWords[i].count("<")==0 and reversedWords[i+1].count("<")==0:
        print(reversedWords[i],end=" ")
    else: 
        print(reversedWords[i],end="")

print(reversedWords[len(reversedWords)-1])




        
        





