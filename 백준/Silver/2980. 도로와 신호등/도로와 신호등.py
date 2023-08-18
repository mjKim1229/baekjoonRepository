import sys 
input = sys.stdin.readline 

trafficNum, roadLength = map(int,input().rstrip().split())

trafficLightTimes = dict()
trafficLocation = []
for _ in range(trafficNum):
    trafficInfos = list(map(int,input().rstrip().split()))
    trafficLocation.append(trafficInfos[0])
    trafficLightTimes[trafficInfos[0]]=(trafficInfos[1:])

timeCount = 0 
for nowLocation in range(roadLength):
    #print("timeCount",nowLocation,timeCount) 
    if nowLocation in trafficLocation:
        redLigthTime,GreenLightTime = trafficLightTimes[nowLocation]
        trafficDescision = timeCount % (redLigthTime+GreenLightTime)
        #print("check",nowLocation,timeCount,trafficDescision)
        if trafficDescision <redLigthTime: 
            timeCount += (redLigthTime - trafficDescision)
            timeCount += 1
        else: 
            timeCount +=1 
    else:
        timeCount +=1   
print(timeCount)