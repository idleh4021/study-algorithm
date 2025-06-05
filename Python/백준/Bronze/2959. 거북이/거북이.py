arr = list(map(int,input().split()))
arr = sorted(arr)
print( min([arr[0],arr[-1]]) * max(arr[1],arr[-2]) )