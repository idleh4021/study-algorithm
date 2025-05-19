import sys
while(True):
    a= sys.stdin.readline()
    if a=="":
        break
    else:
        a,b = map(int, a.split())
        print(b//(a+1))