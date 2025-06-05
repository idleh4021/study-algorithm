a,b,c = map(int,input().split())
if a== b+c or a==b-c or a==b*c or a==b/c:
    print(f'{a}={b}{"+" if a==b+c else "-" if a==b-c else "*" if a==b*c else "/"}{c}')
if c== b+a or c==a-b or c==b*a or c==a/b:
    print(f'{a}{"+" if c==b+a else "-" if c==a-b else "*" if c==b*a else "/"}{b}={c}')