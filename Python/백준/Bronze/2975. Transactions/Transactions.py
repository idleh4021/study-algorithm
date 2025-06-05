while True:
    s,t,p = input().split()
    
    s,p = int(s),int(p)
    if s == p==0 : break
    s+= p if t=='D' else -p
    if s < -200:
        print('Not allowed')
    else : print(s)
    