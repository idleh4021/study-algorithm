n = int(input())
min = 0
max =1
gap =6
cnt = 1
while True:
    if(min<=n and n<=max):
        break   
    else:
        min = max + 1
        max = max + gap
        gap += 6
        cnt += 1
print(cnt)