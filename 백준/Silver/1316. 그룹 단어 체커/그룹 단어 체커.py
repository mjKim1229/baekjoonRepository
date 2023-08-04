import sys 
input = sys.stdin.readline 

wordNumber = int(input().rstrip())
words = []

for _ in range(wordNumber):
    words.append(input().rstrip()) 


count = 0 
for word in words:
    error = 0  
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            newWord = word[index+1:]
            #print("new",newWord)
            if newWord.count(word[index]) >= 1: 
                error +=1
    #print("erorr",word,error)           
    if error ==0:
        count +=1 

print(count)   
        
        
        
