import sys
a,b = map(int,sys.stdin.readline().strip('\n').split())
a_p= [a//4-1 if a%4==0 else a//4,4 if a%4==0 else a%4]
b_p= [b//4-1 if b%4==0 else b//4,4 if b%4==0 else b%4]
answer = sum([abs(a_p[0]-b_p[0]), abs(a_p[1]-b_p[1])])

print(answer)