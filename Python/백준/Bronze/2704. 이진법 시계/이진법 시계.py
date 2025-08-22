for _ in range(int(input())):
    arr = list(map(int,input().split(':')))
    bin_arr =list( map(lambda x: f'{x:06b}' , arr))
    #print(bin_arr)
    for i in range(6):
        for j in bin_arr:
            print(j[i], end='')
    
    print(' ' + ''.join([f'{i}' for i in bin_arr]))
