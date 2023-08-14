import sys 
input = sys.stdin.readline 

testNum = int(input().rstrip())

destination = [(-1,0),(0,1),(1,0),(0,-1)]
currentDestination = 0 


#0->N, 1-> E , 2-> S, 3-> W
def changeDestination(destinationShift):
    global currentDestination
    if destinationShift == 'R':
        if currentDestination == 3: 
            currentDestination = 0 
        else: 
            currentDestination +=1  
    elif destinationShift == 'L':
        if currentDestination == 0: 
            currentDestination = 3
        else: 
            currentDestination -= 1  

def checkMaxMin(currentX,currentY):
    global xMin, xMax , yMin , yMax
    if xMin > currentX: 
        xMin = currentX
    elif xMax < currentX: 
        xMax = currentX
    elif yMin > currentY: 
        yMin = currentY
    elif yMax < currentY: 
        yMax = currentY



for _ in range(testNum):
    todoList = list(input().rstrip())
    xMin, xMax , yMin , yMax = 0,0,0,0
    location = [0,0]
    for do in todoList: 
        if do =='F':
            location[0] += destination[currentDestination][0]
            location[1] += destination[currentDestination][1]
            checkMaxMin(location[0],location[1])
        elif do =='B': 
            location[0] -= destination [currentDestination][0]
            location[1] -= destination[currentDestination][1]
            checkMaxMin(location[0],location[1])
        elif do == 'L': 
            changeDestination(do)
        elif do == 'R':
            changeDestination(do)
    print((xMax-xMin)*(yMax-yMin))
    


