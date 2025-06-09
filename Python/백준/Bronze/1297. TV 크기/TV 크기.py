import sys
a,b,c = map(float,sys.stdin.readline().strip('\n').split())

v = (a**2/(b**2+c**2))**0.5
print(int(v*b),int(v*c))

