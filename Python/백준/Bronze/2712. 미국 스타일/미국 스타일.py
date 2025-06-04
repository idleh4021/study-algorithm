unt ={'kg': 2.2046, 'lb': 0.4536, 'l': 0.2642, 'g': 3.7854}
conv = {'kg': 'lb', 'lb': 'kg', 'l': 'g', 'g': 'l'}
for _ in range(int(input())):
    a, b = input().split()
    a = float(a)
    print(f'{a * unt[b]:.4f} {conv[b]}')