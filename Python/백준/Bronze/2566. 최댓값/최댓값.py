max_val = 0
row_val = 0
col_val = 0
for i in range(9):
    c = input().split()
    c = [int(i) for i in c]
    tmp_max_val = max(c)
    idx = c.index(tmp_max_val)
    if max_val<tmp_max_val:
        max_val = tmp_max_val
        row_val = i
        col_val = idx
    
print(max_val)
print(str(row_val+1)+' '+str(col_val+1))