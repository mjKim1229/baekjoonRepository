x = int(input())

a = 100 
count = 99 

if x <= 99: 
    print(x)
else:
    for i in range(a,x+1):
        first =  i//100 
        second = i//10 - (first*10) 
        third = i%10
        if first - second == second - third:  
            count +=1
    print(count) 
