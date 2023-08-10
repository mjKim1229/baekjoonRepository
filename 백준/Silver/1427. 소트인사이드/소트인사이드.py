import sys 
input = sys.stdin.readline 

number = input().rstrip()

listNumber = []

for n in number: 
    listNumber.append(n)

listNumber.sort(reverse=True)

print("".join(listNumber))