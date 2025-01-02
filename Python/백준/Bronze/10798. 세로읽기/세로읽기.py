a=[''] * 15

for i in range(5):
    str_val = input()
    for j in range(len(str_val)):
        a[j]+=str_val[j]
print(''.join([i for i in a if i!='']))