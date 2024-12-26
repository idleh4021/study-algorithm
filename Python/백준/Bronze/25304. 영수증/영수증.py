sum_val = int(input())
cnt = int(input())
answer = 0
for i in range(cnt):
    p,q = input().split()
    answer+= int(p)*int(q)

print('Yes' if sum_val == answer else 'No')