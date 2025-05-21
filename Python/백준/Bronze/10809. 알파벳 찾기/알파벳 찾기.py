alphabet = "abcdefghijklmnopqrstuvwxyz"
dc = {}
for c in alphabet:
    dc[c]=-1    

s = input()
for c in s:
    if dc[c] == -1:
        dc[c] = s.index(c)

print(*dc.values())
