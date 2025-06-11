import sys
a=sys.stdin.readline().strip('\n')
arr = list(map(int, sys.stdin.readline().strip('\n').split()))
c = int(sys.stdin.readline().strip('\n'))
answer =0 
for i in arr:
    answer+=(i//c)*c+ (0 if i%c==0 else c)
print(answer)

