import sys
a,b = map(str,sys.stdin.readline().strip('\n').split())
answer = int(a,2)+int(b,2)
print('{0:b}'.format(answer))
