while(True):
    a,b =map(int,input().split())
    if a==b and b==0:
        break
    else :
        print('Yes' if a>b else 'No')