import sys
import math  
input = sys.stdin.readline 

roomNumber = input().rstrip()

maximum = 1 
for i in range(0,9):
    if i ==6:
        nineCount =roomNumber.count('9') 
        sixCount = roomNumber.count(str(i))
        nowIndexCount = math.ceil((nineCount+sixCount)/2)
        #print(nineCount,sixCount,(nineCount+sixCount)/2,math.ceil((nineCount+sixCount)/2))
    else:
        nowIndexCount = roomNumber.count(str(i))
    
    if nowIndexCount > maximum: 
        maximum = nowIndexCount

print(maximum)