a,b,c = map(int,input().split())
qty = min([a//2,b])
rests = (a-2*qty)+(b-qty)
if rests >= c:
    print(qty)
else: 
    minus = c-rests
    qty -= minus//3+(1 if minus%3 !=0 else 0)
    print(qty)