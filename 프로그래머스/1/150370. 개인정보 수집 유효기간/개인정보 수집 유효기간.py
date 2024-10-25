from collections import defaultdict

plus_dict = defaultdict(int)
answer = []

def initiate_plus_dict(terms):
    for term in terms:
        type, month = term.split(" ")
        plus_dict[type] = int(month) * 28 

def check_privacy(i, date, type, today):
    f_year, f_month, f_day = list(map(int, date.split(".")))
    t_year, t_month, t_day = list(map(int, today.split(".")))
    year = (t_year - f_year) * 336 
    month = (t_month - f_month) * 28
    day = t_day - f_day 
    total = year + month + day 
    if total >= plus_dict[type]:
        answer.append(i+1)

def solution(today, terms, privacies):
    # 초기화
    global answer
    answer = []
    plus_dict.clear()

    initiate_plus_dict(terms)
    for i, privacy in enumerate(privacies):
        date, type = privacy.split(" ")
        check_privacy(i, date, type, today)

    return answer
