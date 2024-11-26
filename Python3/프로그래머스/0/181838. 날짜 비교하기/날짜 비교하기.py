import datetime as dt
def solution(date1, date2):
    dt_date1 = dt.datetime(date1[0],date1[1],date1[2])
    dt_date2 = dt.datetime(date2[0],date2[1],date2[2])
    return int(dt_date1<dt_date2)