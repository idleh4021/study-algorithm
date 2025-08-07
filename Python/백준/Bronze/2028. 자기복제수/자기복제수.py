T = int(input())
for _ in range(T):
    n = int(input())
    result = str(n**2)
    if(str(n) == str(result[-len(str(n)):])):
        print('YES')
    else:
        print('NO')
