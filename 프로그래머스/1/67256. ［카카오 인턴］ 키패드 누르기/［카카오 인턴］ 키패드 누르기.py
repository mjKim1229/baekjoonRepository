#거리 구하는 함수 
#왼손잡이 오른손 잡이 
#현재 위치 반환 


#키패드 배열 
keyPad = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),
         7:(2,0),8:(2,1),9:(2,2),"*":(3,0),0:(3,1),"#":(3,2)}
leftKey = {1,4,7}
rightKey = {3,6,9}

def calculateDistance(leftLoc, rightLoc, numberLoc,hand): 
    leftDist = abs(leftLoc[0] - numberLoc[0]) + abs(leftLoc[1] - numberLoc[1])
    rightDist =  abs(rightLoc[0] - numberLoc[0]) + abs(rightLoc[1] - numberLoc[1])
    if leftDist > rightDist: 
        return "R"
    elif leftDist < rightDist:
        return "L"
    else:
        if hand == "left": 
            return "L"
        else: 
            return "R"
        

def solution(numbers, hand):
    answer = ''
    global keyPad, leftKey, rightKey
    leftLoc = keyPad["*"]
    rightLoc = keyPad["#"]
    for number in numbers:
        if number in leftKey: 
            answer += "L"
            leftLoc = keyPad[number]
        elif number in rightKey: 
            answer += "R"
            rightLoc = keyPad[number]
        else:
            calHand = calculateDistance(leftLoc,rightLoc,keyPad[number],hand)
            if calHand == "L":
                leftLoc = keyPad[number]
            else: 
                rightLoc = keyPad[number]
            answer += calHand 
    
    return answer