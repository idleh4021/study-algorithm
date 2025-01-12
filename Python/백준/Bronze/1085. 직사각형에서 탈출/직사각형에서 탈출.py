x,y,w,h = input().split()
x,y,w,h = int(x),int(y),int(w),int(h)


print(min([abs(x-w),abs(y-h),x,y]))