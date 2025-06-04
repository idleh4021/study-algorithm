import sys
a,b = map(int,sys.stdin.readline().strip('\n').split())

num = 0
for i in range(2,b):
    if(a%i==0) :
        num=i
        break
    
if num == 0:
    print('GOOD')
else:
    print('BAD', num)
    
