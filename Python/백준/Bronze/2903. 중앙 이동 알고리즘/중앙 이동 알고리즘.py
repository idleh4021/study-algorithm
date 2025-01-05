cnt = int(input())
sqrs= 1
lines = 4
dots = 4
val_to_lines = 1

for i in range(1,cnt+1):
    dots +=sqrs+lines
    sqrs = 4**i
    lines = lines*4 - (4*val_to_lines)
    val_to_lines*=2


print(dots)


