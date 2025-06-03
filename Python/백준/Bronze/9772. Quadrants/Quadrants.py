while True:
    a,b = map(float,input().split())
    if a==0 or b==0:
        print('AXIS')
    elif a>0:
        print('Q1' if b>0 else 'Q4')
    else:
        print('Q2' if b>0 else 'Q3')
    if a==b==0:
        break