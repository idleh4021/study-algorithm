from datetime import date
while True:
    d,m,y = map(int,input().split())
    if d==m==y==0:
        break
    try:
        d = date(y,m,d)
        print('Valid')
    except:
        print('Invalid')
