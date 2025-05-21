t = int(input())
for i in range(t):
    h,w,n = map(int, input().split())
    if(n%h==0):
        xx= n//h
        yy= h
    else :
        xx= n//(h)
        xx+=1
        yy= n%(h)
    print(f'{yy}{xx:02d}')