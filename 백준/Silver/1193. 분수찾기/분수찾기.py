import sys 
input = sys.stdin.readline 

n = int(input().rstrip())


bunmo = 1
bunja = 0 
while True:
    if bunmo < n: 
        n -= bunmo
        bunmo +=1
    else: 
        bunja = n
        break 

#print("start",bunmo,bunja)

a = 0
b = 0  
if bunmo %2 ==0:
    a = bunja 
    b = bunmo - a+1
else:
    b = bunja   
    a = bunmo - b+1 
    
print(a, '/', b, sep='')


        


          

