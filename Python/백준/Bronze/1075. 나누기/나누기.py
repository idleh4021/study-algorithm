import sys
a=sys.stdin.readline().strip('\n')
b= int(sys.stdin.readline().strip('\n'))

c=0
for i in range(100):
    a= a[:len(a)-2]+f'{c:02d}'
    if( int(a) %b ==0):
        print(f'{c:02d}')
        break
    c+=1
