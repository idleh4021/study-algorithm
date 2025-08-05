def getCnt(arr): 
    max_h = 0
    cnt = 0
    for i in arr:
        if i > max_h:
            max_h = i
            cnt += 1
    return cnt
        

N = int(input())
cups = []
for _ in range(N):
    cups.append(int(input()))

print(getCnt(cups))
print(getCnt(cups[::-1]))


