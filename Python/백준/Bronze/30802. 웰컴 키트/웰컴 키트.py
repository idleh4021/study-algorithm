n = int(input())
t_sizes = list(map(int, input().split()))
t_unit,p_unit = map(int, input().split())
p_unit_qty,p_qty = n//p_unit,n%p_unit
t_unit_qty=0
for i in t_sizes:
    t_unit_qty += i//t_unit
    t_unit_qty += 1 if i%t_unit != 0 else 0

print(t_unit_qty)
print(f'{p_unit_qty} {p_qty}')