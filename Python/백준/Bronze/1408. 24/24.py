import datetime as dt
current_dt = dt.datetime.now()
h,m,s = map(int, input().split(':'))
current_dt = current_dt.replace(hour=h, minute=m, second=s)
st_dt =  dt.datetime.now()
h,m,s = map(int, input().split(':'))
st_dt = st_dt.replace(hour=h, minute=m, second=s)
diff=  st_dt -current_dt
print(f'{diff.seconds//3600:02}:{(diff.seconds//60)%60:02}:{diff.seconds%60:02}')
