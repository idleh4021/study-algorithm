a,b,c = map(int,input().split())
arr = sorted([a,b,c])
if(a==b==c):
    print(2)
elif arr[0]**2+arr[1]**2 == arr[2]**2:
    print(1)
else:
    print(0)