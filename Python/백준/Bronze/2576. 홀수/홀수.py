import sys
nums =[]
for _ in range(7):
    a = int(sys.stdin.readline().strip('\n'))
    if a%2==1: nums.append(a)
if(len(nums) == 0):
    print(-1)
else:
    print(sum(nums))
    print(min(nums))