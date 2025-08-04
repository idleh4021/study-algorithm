p = {}
n = input()
arr = list(map(int, input().split()))
answer =0
for i in arr:
    if i in p.keys():
        answer+=1
    else:
        p[i] = 1
print(answer)