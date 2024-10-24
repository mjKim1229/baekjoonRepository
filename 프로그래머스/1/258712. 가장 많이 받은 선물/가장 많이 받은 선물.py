# def run_last_month(gifts, last_month):
from collections import defaultdict 
name_index = defaultdict(int)

def make_index(friends):
    for i in range(len(friends)):
        name_index[friends[i]] = i 
    
def run_last_month(gifts, last_month, gift_list):
    for gift in gifts:
        a, b = gift.split()
        a_index = name_index[a]
        b_index = name_index[b]
        last_month[a_index][b_index] += 1 
        gift_list[a_index] += 1 
        gift_list[b_index] -= 1 
    return last_month, gift_list

def is_given(i, j, last_month):
    if last_month[i][j] > 0 or last_month[j][i] > 0:
        return True 

def is_same(i, j, last_month):
    if last_month[i][j] == last_month[j][i]:
        return True 
    
def run_this_month(gift, last_month, gift_list, N, this_month_gifts):
    for i in range(N):
        for j in range(i+1, N):
            print(i,j)
            #주고 받음 & 서로 개수 다름 
            if is_given(i,j, last_month) and not is_same(i,j,last_month) :
                if last_month[i][j] > last_month[j][i]:
                    this_month_gifts[i] += 1 
                else: 
                    this_month_gifts[j] += 1 
            elif not is_given(i,j, last_month) or is_same(i,j,last_month):
                if gift_list[i] > gift_list[j]:
                    this_month_gifts[i] += 1 
                elif gift_list[i] < gift_list[j]:
                    this_month_gifts[j] += 1 
    return this_month_gifts 
                
                    
                
                
    

def solution(friends, gifts):
    N = len(friends)
    last_month = [[0] * N for _ in range(N)]
    gift_list = [0] * N
    this_month_gifts = [0] * N
    
    make_index(friends)
    last_month, gift_list = run_last_month(gifts, last_month, gift_list)
    answer = run_this_month(gifts, last_month, gift_list, N, this_month_gifts)
    print(last_month)
    return max(answer)
    
    
    
    