for _ in range(int(input())):
    a,b = input().split()
    idx = int(a)-1
    arr = list(b)
    del arr[idx]
    print(*arr, sep='')
    
    