t = int(input())
for i in range(t):
    a,s = input().split()
    a = int(a)
    print(''.join(i*a for i in s))