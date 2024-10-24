from itertools import product

max_plus_count, max_price_sum = 0, 0 

def update_answer(plus_count, e_sum):
    global max_plus_count, max_price_sum
    if plus_count > max_plus_count:
        max_plus_count = plus_count 
        max_price_sum = e_sum 
    elif plus_count == max_plus_count and e_sum > max_price_sum:
        max_price_sum = e_sum 
    #print(max_price_sum, e_sum)
        
    


def calculate_user_plus(buy_money_list, users):
    plus_count, e_sum = 0, 0 
    for i in range(len(users)):
        if buy_money_list[i] >= users[i][1]:
            plus_count += 1 
        else: 
            e_sum += buy_money_list[i]
    
    update_answer(plus_count, e_sum)
    #print(plus_count, e_sum)

def discount_run(discounts, emoticons, users):
    #print(discounts)
    buy_money_list = []
    for user in users:
        temp_sum = 0 
        discount_edge = user[0]
        for i in range(len(discounts)):
            if discounts[i] >= discount_edge:
                temp_sum += (emoticons[i] * ((100 - discounts[i]) /100))
        buy_money_list.append(temp_sum)
    calculate_user_plus(buy_money_list, users)
    #print(buy_money_list)

visited = [False] * 4
def dfs(e_length, discounts, discount_list, emoticons, users):
    if len(discounts) == e_length:
        discount_run(discounts, emoticons, users)
        return 
        
    for i in range(4):
        discounts.append(discount_list[i])
        dfs(e_length, discounts, discount_list, emoticons, users)
        discounts.pop()
        

def solution(users, emoticons):
    global max_plus_count, max_price_sum
    discount_list = [10,20,30,40]
    visited = [False] * 4
    e_length = len(emoticons)
    dfs(e_length, [], discount_list, emoticons, users)
        
    return [max_plus_count, max_price_sum]
        