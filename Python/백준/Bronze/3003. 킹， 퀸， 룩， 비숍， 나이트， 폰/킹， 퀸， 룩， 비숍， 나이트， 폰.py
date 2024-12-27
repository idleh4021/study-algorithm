chess = [1,1,2,2,2,8]
arr = input().split()
print(' ' .join([str(val - int(arr[i])) for i,val in enumerate(chess)]))