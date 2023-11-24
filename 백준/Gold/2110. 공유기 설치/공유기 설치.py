import sys 
input = sys.stdin.readline 

hubs = []


def install(distance):
    count = 1  
    left, right = 0,1 
    while right < n: 
        if hubs[right] - hubs[left] >= distance:
            count +=1
            left, right = right, right+1 
        else: 
            right +=1
    return count 

def binary_search(left, right): 
    answer = 1 
    while left <= right: 
        mid = (left + right) //2 
        count = install(mid)

        if c > count:
            right = mid -1  
        else:
            left = mid +1 
            answer = mid
     
    
    return answer  
            
n, c = map(int, input().split())
hubs = [int(input()) for _ in range(n)]

hubs.sort()

print(binary_search(1,hubs[-1]-hubs[0]))

