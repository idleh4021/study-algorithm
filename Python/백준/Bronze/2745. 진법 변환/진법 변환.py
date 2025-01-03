answer=0
val,jin = input().split()
jin = int(jin)
val_l = len(val)

for i in range(val_l):
    answer+=(int(val[i]) if val[i].isdigit() else ord(val[i])-55)*(jin**((val_l-1)-i))

print(answer)