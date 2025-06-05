idx = 0
max_v = 0
for i in range(5):
    val = sum(list(map(int, input().split())))
    
    if val > max_v:
        max_v = val
        idx = i+1

print(idx,max_v)