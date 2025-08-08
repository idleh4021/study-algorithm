def SumFunc(s):
    while(True):
        val = sum([int(i) for i in s])
        if val>9:
            s= str(val)
            continue
        else:
            break
    return val
    

while True:
    a = input()
    if a=='0':break
    else: print(SumFunc(a))
    
    
