import sys 
input = sys.stdin.readline 

row, column = map(int,input().rstrip().split())

weather = []

for i in range(row): 
    weather.append(list(input().rstrip())) 
#print(weather)

for i in range(row):
    cloud = -1  
    for j in range(column):
        if weather[i][j] == 'c':
            cloud = 0
        elif weather[i][j] == '.' and cloud !=-1:
            cloud +=1 
        weather[i][j] = str(cloud)    



for row in weather: 
    print(" ".join(row))



