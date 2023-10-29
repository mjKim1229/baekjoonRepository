x = int(input())

a = 100 
count = 99 

if x <= 99: 
    print(x)
else:
    for i in range(a,x+1):
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]: 
            count +=1 
    print(count)     
