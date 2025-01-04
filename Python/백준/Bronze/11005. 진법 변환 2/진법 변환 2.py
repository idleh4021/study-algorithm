answer=''
val,jin = input().split()
jin = int(jin)
val_l = len(val)
val =int(val)
max_p = 0

while True:
    if val //(jin)**max_p>=1:
        max_p+=1
    else :
        break

for i in range(max_p):
    s = max_p-1-i
    temp_val = val //(jin**s)
    val = val % (jin**s)
    answer+=str(temp_val) if temp_val <10 else chr(temp_val+55)

print(answer)