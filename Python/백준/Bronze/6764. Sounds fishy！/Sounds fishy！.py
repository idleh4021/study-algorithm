
a= []
for i in range(4):
    a.append(int(input()))

if len(set(a))!= len(a) and len(set(a)) != 1:
    print("No Fish")

elif a[0] == a[1] == a[2] == a[3]:
    print("Fish At Constant Depth")
elif a == sorted(a):
    print("Fish Rising")
elif a == sorted(a, reverse=True):
    print("Fish Diving")
else:
    print("No Fish")