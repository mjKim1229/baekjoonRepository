from collections import defaultdict 
import math 
inCar = defaultdict(list)
carTimes = defaultdict(int)
checkInOut = defaultdict(int)
carFees = defaultdict(int)

def addCarTime(carNum,outHour,outMinute):
    global inCar, carTimes 
    inCarTime = inCar[carNum]
    inHour, inMinute = inCarTime[0], inCarTime[1]
    inCarTotalMinutes = inHour * 60 + inMinute 
    outCarTotalMinutes = outHour * 60 + outMinute 
    carTimes[carNum] += outCarTotalMinutes - inCarTotalMinutes
    
    
    
def calculateFee(carNum,totalMinutes,fees):
    defaultMinute, defaultFee = fees[0], fees[1]
    perTime, perFee = fees[2], fees[3]
    if totalMinutes <= defaultMinute: 
        return defaultFee
    else: 
        return defaultFee + perFee * math.ceil((totalMinutes-defaultMinute)/perTime)
    
    
def solution(fees, records):
    answer = []
    global inCar , carTimes, checkInOut 
    
    for record in records: 
        time, carNum, inOut = record.split()
        hour, minute = time.split(":")
        if inOut == "IN": 
            inCar[carNum] = [int(hour),int(minute)]
            checkInOut[carNum] += 1
        else:
            addCarTime(carNum,int(hour),int(minute))
            checkInOut[carNum] -=1 
    
    #out 안한 차들 시간 추가 
    for carNum, checkOut in checkInOut.items(): 
        if checkOut != 0:
            addCarTime(carNum,23,59)
    
    for carNum, totalMinutes in carTimes.items():
        global carFees
        fee = calculateFee(carNum, totalMinutes,fees)
        print(carNum,fee)
        carFees[carNum] += fee
    
    resultDict = sorted(carFees)       
    for carNum in resultDict: 
        answer.append(carFees[carNum])
    return answer
            
            
    