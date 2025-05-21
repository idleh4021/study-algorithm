arr = list(map(int, input().split()))
a= [idx for idx,val in enumerate(arr) if val>0]
#print(a)
cnt_z =len([i for idx,i in enumerate(arr) if idx > a[0] and idx < a[-1]])
answer =( arr[a[-1]] - arr[a[0]]) / (cnt_z + 1)
if answer %1 !=0:
    print(-1)
else:
    print(' '.join(str(int((idx-a[0])*answer+arr[a[0]])) for idx,i in enumerate(arr)))