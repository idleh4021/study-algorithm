l = input().split()
l = sorted([int(i) for i in l])
l[-1] = l[-1] if l[0]+l[1]>l[-1] else l[0]+l[1]-1

print(sum(l))