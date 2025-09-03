dwarf =[]
for _ in range(9):
    dwarf.append(int(input()))

gap = sum(dwarf)-100

for i in range(gap):
    a,b = i+1,gap - (i+1)
    if a in dwarf and b in dwarf:
        dwarf.remove(a)
        dwarf.remove(b)
        break

print(*dwarf,sep='\n')