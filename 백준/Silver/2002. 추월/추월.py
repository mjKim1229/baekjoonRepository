import sys 
input = sys.stdin.readline 

enter = dict()
out = []
carNum = int(input().rstrip()) 


for i in range(carNum):
    carAlpha = input()
    enter[carAlpha] = i

for _ in range(carNum):
    out.append(input()) 

count =0 
for i in range(carNum-1): 
    for j in range(i+1,carNum):
        if enter[out[i]] > enter[out[j]]:
            count+=1 
            break  

print(count)