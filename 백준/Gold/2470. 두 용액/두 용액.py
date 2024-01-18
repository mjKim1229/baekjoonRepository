import sys 
input = sys.stdin.readline 

n = int(input().rstrip())

#[-99, -2, -1, 4, 98]
array = list( map(int,input().rstrip().split()) ) 

array.sort()

left, right = 0 , n-1  

INF = int(1e9)
leftAnswer, rightAnswer, gap = array[left],array[right], abs(array[right]+array[left])

while left < right:
    #print(left,right)
    tempSum = array[left] + array[right]
    tempGap = abs(tempSum)
    #print(tempGap)
    if tempGap < gap: 
        leftAnswer, rightAnswer, gap = array[left], array[right], tempGap
    
    if tempSum > 0:
        right -= 1 
    elif tempSum < 0: 
        left +=1
    else: 
        break 

print(leftAnswer,rightAnswer)

