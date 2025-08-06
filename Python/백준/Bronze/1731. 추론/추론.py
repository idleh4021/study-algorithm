cnt = int(input())
f,s,c = 0,0,0
gap = 1
for i in range(cnt):
    val = int(input())
    if f == 0 : f = val
    elif s == 0 : s = val
    elif c == 0 : c = val

if(abs(f-s) == abs(s-c)):
    gap = abs(f-s)
    print(f +(gap * cnt))
else:
    gap = s//f
    print(f * (gap**cnt))