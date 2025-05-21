t = list(map(int, input().split()))
asc = sorted(t)
dsc = sorted(t, reverse=True)
if t == asc:
    print("ascending")
elif t == dsc:
    print("descending")
else:
    print("mixed")

