import sys 
input = sys.stdin.readline 

n = int(input().rstrip()) 
haveList = sorted(list(map(int,input().rstrip().split())))

m = int(input().rstrip()) 
checkList = list(map(int,input().rstrip().split()))

def binarySearch(array,target,start,end):
    if start > end: 
        return 0 
    mid = (start+end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target: 
        return binarySearch(array,target,start,mid-1)
    else: 
        return binarySearch(array,target,mid+1,end)

for num in checkList:
    print(binarySearch(haveList,num,0,n-1))