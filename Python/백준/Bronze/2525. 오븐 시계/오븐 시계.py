from datetime import datetime,timedelta


t = datetime.strptime(input(),'%H %M')
t= t + timedelta(minutes=int(input()))

print(str(t.hour) + ' '+str(t.minute))