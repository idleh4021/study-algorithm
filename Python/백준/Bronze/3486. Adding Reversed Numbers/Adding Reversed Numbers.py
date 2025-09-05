def reverseInt(val):
    s  = str(val)
    return int(s[::-1])

for _ in range(int(input())):
    a,b = map(int,input().split())
    answer = reverseInt(a)+reverseInt(b)
    print(reverseInt(answer))
