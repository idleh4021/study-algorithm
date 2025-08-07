frm = int(input())
to = int(input())
arr =[]
for i in range(frm,to+1):
    if (i**0.5)% 1 ==0:
        arr.append(i)

if len(arr)>0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)