while True:
    wives = float(input())
    if(wives==0) : break
    socks= wives*wives
    cats = socks*wives
    kitties = cats*wives
    print(f'{round(1+socks+cats+kitties+wives,2):.2f}')