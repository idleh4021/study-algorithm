import sys
a,b = sys.stdin.readline().strip('\n').split()
print( int(str(int(a[::-1])+int(b[::-1]))[::-1]) )
