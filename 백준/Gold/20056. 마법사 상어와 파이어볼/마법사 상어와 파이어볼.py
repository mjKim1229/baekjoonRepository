import sys 
input = sys.stdin.readline
from collections import defaultdict
import copy, math 
#N X N 격자 
#M : 파이어볼 개수 
#i번 위치 ri ci / di 속력 / mi 질량 
# 1 ~ N 

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
#process 
#방향 di로 속력 si칸 만큼 이동 

#칸에 여러개의 파이어볼 
# 합쳐짐 
# 4개로 나눠ㅣ어짐 
# 질량 : 질량합 / 5 
# 속력 : 속력합 / 합쳐진 개수 
# 방향 모두 홀수 , 짝수 = 0,2,4,6 or 1,3,5,7 
#질량 0 : 소멸 

N, M, K = map(int, input().rstrip().split())
fireballs = defaultdict(list)
for i in range(M):
    r, c, m, s, d = map(int, input().rstrip().split())
    fireballs[(r-1,c-1)].append((m,s,d))

def move_fireballs():
    global fireballs
    new_fireballs = defaultdict(list)
    for loc, info_list in fireballs.items():
        x, y = loc 
        for m, s, d in info_list:
            nx = (x + dx[d] * s) % N 
            ny = (y + dy[d] * s) % N 
            new_fireballs[(nx,ny)].append((m,s,d))
    
    fireballs = new_fireballs.copy()
 
def all_odd_or_even(dirs):
    odd_flag, even_flag = False, False 
    for d in dirs: 
        if d % 2 == 1:
            odd_flag = True 
        if d % 2 == 0:
            even_flag = True 
    if odd_flag and even_flag:
        return False 
    return True 

def change_duplicate_fireballs():
    global fireballs
    new_fireballs = defaultdict(list)

    for loc, info_list in fireballs.items():
        if len(info_list) == 1:
            new_fireballs[loc].append(info_list[0])
            continue
        
        sum_m , sum_s, dirs = 0,0,[]
        for m, s, d in info_list:
            sum_m += m 
            sum_s += s 
            dirs.append(d)
        new_m = int(sum_m/5)
        if new_m == 0:
            continue
        new_s = int(sum_s/len(info_list))
        new_dirs = [0,2,4,6] if all_odd_or_even(dirs) else [1,3,5,7]
        
        for new_d in new_dirs: 
            new_fireballs[loc].append((new_m,new_s,new_d))
        
    fireballs = new_fireballs.copy()
        
for _ in range(K):
    move_fireballs()
    change_duplicate_fireballs()

result = 0 
for loc, info_list in fireballs.items():
    for m, s, d in info_list:
        result += m 

print(result)