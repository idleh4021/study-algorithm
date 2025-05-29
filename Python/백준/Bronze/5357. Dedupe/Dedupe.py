for _ in range(int(input())):
    s = input()
    answer = [i for idx,i in enumerate(s) if idx== 0 or s[idx-1] != s[idx] ]
    print(''.join(answer))
    