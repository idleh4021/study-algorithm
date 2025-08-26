arr = input().split()
min = sum([int(i.replace('6','5')) for i in arr])
max = sum([int(i.replace('5','6')) for i in arr])

print(min,max)