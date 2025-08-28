import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
year = 2009
d,m = map(int,input().split())
dt =datetime.date(year,m,d)
print(days[dt.weekday()])