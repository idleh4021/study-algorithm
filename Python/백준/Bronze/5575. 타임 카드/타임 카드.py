import datetime
for _ in range(3):
    a = list(map(int, input().split()))
    in_time = datetime.datetime.now().replace(hour=a[0], minute=a[1], second=a[2])
    out_time = datetime.datetime.now().replace(hour=a[3], minute=a[4], second=a[5])
    diff = out_time - in_time
    print(diff.seconds //3600 , diff.seconds // 60 % 60, diff.seconds % 60)
    
    