from collections import defaultdict

plus_dict = defaultdict(int)
answer = []

def plus_month(f_year, f_month, type):
    plus_month = plus_dict[type]
    total_months = f_month + plus_month

    # 연도 계산
    if total_months > 12:
        f_year += (total_months - 1) // 12
    f_month = (total_months - 1) % 12 + 1

    return f_year, f_month

def initiate_plus_dict(terms):
    for term in terms:
        type, month = term.split(" ")
        plus_dict[type] = int(month)

def check_over(f_year, f_month, f_day, today, i):
    t_year, t_month, t_day = map(int, today.split("."))

    # 날짜가 오늘 이전인지 확인
    if (f_year < t_year or
        (f_year == t_year and f_month < t_month) or
        (f_year == t_year and f_month == t_month and f_day <= t_day)):
        answer.append(i + 1)

def check_privacy(i, date, type, today):
    f_year, f_month, f_day = map(int, date.split("."))
    f_year, f_month = plus_month(f_year, f_month, type)
    check_over(f_year, f_month, f_day, today, i)

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
