import sys 
input = sys.stdin.readline 

S = input().rstrip()
subStringSet= set()
for length in range(1,len(S)+1): 
    for start in range(len(S)-length+1):
        subString = S[start:(start+length)]
        #print(subString)
        subStringSet.add(subString)

print(len(subStringSet))