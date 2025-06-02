import math
a,b,c = map(float,input().split())
gap = abs(a-b)
print(int(math.ceil(gap/c)))
