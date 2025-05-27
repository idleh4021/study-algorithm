from datetime import datetime, timedelta

h,m,s = map(int,input().split())
gap = int(input())
dt = datetime.now()
time = dt.replace(hour=h, minute=m, second=s)
result = time + timedelta(seconds=gap)


print(result.hour,result.minute,result.second)