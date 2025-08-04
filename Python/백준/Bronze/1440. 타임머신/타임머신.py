nums =list( map(int, input().split(':')))

hr = len([i for i in nums if 0<i<13])
#print(0 if nums[0]==nums[1]== nums[2]==0 else hr*2)
print(0 if len([i for i in nums if i >= 60]) else hr*2 )