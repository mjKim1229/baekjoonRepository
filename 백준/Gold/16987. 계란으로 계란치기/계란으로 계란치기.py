import sys 
input = sys.stdin.readline 

def dfs(index, strongs, weights):
    global answer
    #print(index,strongs) 
    if index == n:
        count =0 
        for i in strongs:
            if i <=0: 
                count +=1 
        answer = max(answer, count)
        return 
    nowStrong = strongs[index]
    nowWeight = weights[index]
    for target in range(n):
        if target != index:
            targetStrong = strongs[target]
            targetWeight = weights[target]
            newStrongs = strongs[:]
            #내구도가 0보다 커야 깸 
            #치는 작업 
            if nowStrong > 0 and targetStrong >0:
                newStrongs[index] = nowStrong - targetWeight
                newStrongs[target] = targetStrong - nowWeight 
            dfs(index+1,newStrongs,weights)


n = int(input().rstrip())
strongs = []
weights = []
for i in range(n):
    strong, weight = map(int, input().rstrip().split())
    strongs.append(strong)
    weights.append(weight)

answer = 0 
dfs(0,strongs,weights)
print(answer)