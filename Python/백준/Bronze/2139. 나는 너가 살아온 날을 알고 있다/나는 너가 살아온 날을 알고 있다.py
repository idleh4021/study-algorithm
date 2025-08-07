import datetime  as dt

while True:
    d,m,y = map(int,input().split())        
    if(d==0 and m==0 and y==0) : break
    st_date = dt.datetime(year=y,month=1,day=1)
    ed_date = dt.datetime(year=y,month=m,day=d)
    diff = ed_date-st_date
    print(diff.days+1)
    