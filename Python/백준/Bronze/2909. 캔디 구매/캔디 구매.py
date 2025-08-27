c,k = map(int,input().split())
if k ==0: print(c)
else :
    if len(str(c))>= k and  str(c)[-k] =='5':
        c += 1*(10)**(k-1)

    print(round(c,-k))