n,m = input().split()
arr = ['0']*int(n)
for i in range(int(m)):
    s,e,num = input().split()
    arr[int(s)-1:int(e)] = [str(num)] * len(arr[int(s)-1:int(e)])
print(' '.join(arr))