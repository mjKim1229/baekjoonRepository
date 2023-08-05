import sys 
input = sys.stdin.readline

number , removeIndex = map(int,input().rstrip().split())
removedList = []

visited = [False] * number
graph = [i for i in range(1,number+1)]


index = 0

for i in range(number):
    index += (removeIndex-1)
    if index >= len(graph):
        index = index % len(graph)
        
    #print(graph.pop(index))
    removedList.append(str(graph.pop(index)))

print("<",", ".join(removedList)[:],">", sep='')
     