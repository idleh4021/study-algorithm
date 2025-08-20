for _ in range(int(input())):
    c = input()
    arr = input()
    answer= list(map(lambda x: arr[ord(x) - 65] if x != ' ' else ' ',c))
    print(*answer, sep='') 