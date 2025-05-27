
sum,gap = map(int, input().split())

a = (sum+gap)//2
b = abs(a-gap)

if a+b == sum and a-b == gap:
    print(a, b)
else:
    print(-1)