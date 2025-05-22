r = 31
M = 1234567891
cnt = int(input())
s= input()
answer = 0
for idx,c in enumerate(s):
    answer += (ord(c)-96) * (r**idx)
answer %= M
print(answer)