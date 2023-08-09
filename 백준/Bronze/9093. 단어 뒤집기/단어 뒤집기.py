import sys 
input = sys.stdin.readline 

inputWordNum = int(input().rstrip())



for _ in range(inputWordNum):
    str = input().rstrip()
    words = list(str.split(' '))
    reversedWords = []
    
    for word in words:
        reversedWords.append(word[::-1])

    answer = " ".join(reversedWords)
    print(answer)





    