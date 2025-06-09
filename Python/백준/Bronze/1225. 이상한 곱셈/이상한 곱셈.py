import sys
a,b = map(str,sys.stdin.readline().strip('\n').split())
answer = 0
b_sum =0
b_sum = sum( [int(i) for i in b])
for i in a:
    answer+= int(i)*b_sum

print(answer)