n,m = input().split()
n,m = int(n),int(m)
ar = [i+1 for i in range(n)]
for idx in range(m):
    s,e = input().split()
    s,e = int(s),int(e)
    rever_ar = ar[s-1:e]
    rever_ar.reverse()
    ar[s-1:e] =rever_ar
print(' '.join([str(i) for i in ar]))