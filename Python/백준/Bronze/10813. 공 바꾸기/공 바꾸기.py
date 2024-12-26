n,m = input().split()
b = [i+1 for i in range(int(n))]
for i in range(int(m)):
    o,t = input().split()
    b[int(o)-1],b[int(t)-1] = b[int(t)-1],b[int(o)-1]

print(' '.join([str(i) for i in b]))