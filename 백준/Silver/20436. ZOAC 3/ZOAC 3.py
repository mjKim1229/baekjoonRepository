import sys
input = sys.stdin.readline 

alphabet = [['z','x','c','v','b','n','m','ㅁ','ㅁ','ㅁ'], 
        ['a','s','d','f','g','h','j','k','l','ㅁ'], 
        ['q','w','e','r','t','y','u','i','o','p']]
# 3 x 10 

#행 0 ~ 2
#열 0 ~ 3

left, right = input().rstrip().split()
result = input().rstrip()

def find_location(alpha):
    for i in range(3):
        for j in range(10): 
            if alphabet[i][j] == alpha:
                return i, j 

def left_or_right(x,y):
    if 0<=x<=2 and 0<=y<=4 and not (x == 0 and y == 4):
        return 'LEFT'
    else: 
        return 'RIGHT'

now_left, now_right = left, right
count = 0 
gap = 0 
for i in result:
    t_x, t_y = find_location(i)
    direction = left_or_right(t_x,t_y)
    if direction == 'LEFT': 
        now_x, now_y = find_location(now_left)
        now_left = i
    else: 
        now_x, now_y = find_location(now_right)
        now_right = i
    #print(now_x, now_y, t_x, t_y)
    gap = abs(now_x-t_x) + abs(now_y-t_y)
    #print("gap", gap)
    count += gap
    count += 1 

print(count)
