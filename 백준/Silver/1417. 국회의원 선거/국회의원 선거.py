import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

voteList = []
dasomVote = int(input().rstrip())

for _ in range(n-1): 
    voteList.append(int(input().rstrip())) 

count = 0


if n ==1: 
    print(0)
else:
    while True:
        maxVote = max(voteList)
        if dasomVote > maxVote:
            print(count)
            break
        maxVoteIndex = voteList.index(maxVote)
        voteList[maxVoteIndex] -= 1
        dasomVote += 1 
        count +=1


