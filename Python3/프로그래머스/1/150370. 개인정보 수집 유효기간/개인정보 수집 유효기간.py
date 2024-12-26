import datetime as dt
def solution(today, terms, privacies):
    answer = []
    today_day = date_to_days(today)
    terms_dic = {}
    for term in terms:
        k,v = term.split(' ')
        terms_dic[k]=int(v)
    
    for i in range(len(privacies)):
        dt,k = privacies[i].split(' ')
        day = date_to_days(dt)
        if today_day-day>=month_to_day(terms_dic[k]):
            answer.append(i+1)
    return answer

def month_to_day(month:int):
    return month*28

def year_to_month(year:int):
    return year*12

def date_to_days(date:str):
    src = dt.datetime.strptime(date,'%Y.%m.%d')
    y,m,d = src.year,src.month,src.day
    return month_to_day(year_to_month(y))+month_to_day(m)+d