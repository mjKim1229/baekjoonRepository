import sys 
input = sys.stdin.readline

n = int(input().rstrip())
todoList = list(input().rstrip())

graph = [['#']*100 for _ in range(100)]
nowRow , nowColumn = 50,50 

nowDest = 2
destRow = [-1,0,1,0]
destColumn = [0,1,0,-1]  
def changeDestination(moveDest): 
    global nowDest
    if moveDest == 'R':
        if nowDest == 3: 
            nowDest = 0 
        else: 
            nowDest +=1 
    elif moveDest == 'L': 
        if nowDest == 0: 
            nowDest = 3
        else:
            nowDest -= 1

minRow, maxRow, minCoumn, maxColumn = 50,50,50,50
def checkRange(checkRow, checkColumn):
    global minRow, maxRow, minCoumn, maxColumn
    minRow = min(minRow,checkRow)
    maxRow = max(maxRow, checkRow)
    minCoumn = min(minCoumn, checkColumn)
    maxColumn = max(maxColumn, checkColumn)

            
graph[nowRow][nowColumn] = '.'

for todo in todoList: 
    if todo == 'L' or todo == 'R': 
        changeDestination(todo)
    elif todo == 'F': 
        nowRow += destRow[nowDest]
        nowColumn += destColumn[nowDest]
        graph[nowRow][nowColumn] = '.'
        checkRange(nowRow,nowColumn)

#print(minRow, maxRow, minCoumn, maxColumn)

        

for i in range(minRow,maxRow+1):
    for j in range(minCoumn,maxColumn+1): 
        print(graph[i][j],end="")
    print() 

