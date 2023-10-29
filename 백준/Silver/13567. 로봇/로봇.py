import sys 
input = sys.stdin.readline
xDirection = [0,1,0,-1]
yDirection = [1,0,-1,0]


m,n = map(int, input().rstrip().split())
#print(m,n)

currentDirection = 1
currentLocation = [0,0]

def changeDirection(number):
    global currentDirection 
    if number ==0: 
        if currentDirection ==0:
            currentDirection = 3 
        else: 
            currentDirection -= 1 
    elif number ==1: 
        if currentDirection == 3: 
            currentDirection = 0 
        else: 
            currentDirection +=1  
    #print("현재 방향",currentDirection)

def moveLocation(number):
    global currentLocation 
    tempX = currentLocation[0] + (xDirection[currentDirection] * number)
    tempY = currentLocation[1] + (yDirection[currentDirection] * number)
    #print(tempX,tempY)
    if tempX <0 or tempX > m or tempY <0 or tempY >m: 
        return -1
    else: 
        currentLocation[0] = tempX 
        currentLocation[1] = tempY
        #print("현재 위치",currentLocation)


# instruction, number = input().split()
# print(instruction,number)
# number = int(number)
isError = 0
for i in range(n): 
    if isError == -1: 
        break 
    instruction, number = input().split()
    number = int(number) 
    if instruction == "TURN": 
        changeDirection(number)
    elif instruction == "MOVE": 
        if moveLocation(number) == -1: 
            isError = -1 
            
#print("break")
if isError == 0:
    print(currentLocation[0],currentLocation[1])
elif isError == -1: 
    print(isError)





