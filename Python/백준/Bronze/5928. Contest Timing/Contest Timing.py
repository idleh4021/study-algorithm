import datetime
start_dt = datetime.datetime(2011, 11, 11, 11, 11, 0)
end_arr = list(map(int,input().split()))
end_dt = datetime.datetime(2011, 11, end_arr[0], end_arr[1], end_arr[2],0)
if end_dt < start_dt:
    print(-1)
else:
    delta = end_dt - start_dt
    print(int(delta.total_seconds()//60))