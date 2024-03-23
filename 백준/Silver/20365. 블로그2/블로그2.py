import sys 
input = sys.stdin.readline

n = int(input())
colors = input()

countRed=0 
countBlue =0 
totalCount =0 

for i in range(n):
  if i ==0:
    if colors[i] == 'R': 
      countRed +=1 
    else: 
      countBlue +=1
  else:
    if colors[i] != colors[i-1]: 
      if colors[i] == 'R': 
        countRed += 1 
      else: 
        countBlue +=1
    else: 
      continue
    
#print(countRed,countBlue)
if countRed > countBlue:
  totalCount = 1+ countBlue
elif countRed < countBlue:
  totalCount = 1 + countRed
else:
  totalCount = 1 + countBlue

print(totalCount)