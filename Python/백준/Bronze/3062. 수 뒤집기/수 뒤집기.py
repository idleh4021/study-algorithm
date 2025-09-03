for _ in range(int(input())):
    a = input()
    s = int(a) + int(a[::-1])
    print('YES' if str(s) == str(s)[::-1] else 'NO')