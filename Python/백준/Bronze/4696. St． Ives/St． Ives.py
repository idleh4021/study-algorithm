while True:
    wives = float(input())
    if(wives==0) : break
    socks= wives*wives
    cats = socks*wives
    kitties = cats*wives
    print('{0:.2f}'.format(round(1+socks+cats+kitties+wives,2)))