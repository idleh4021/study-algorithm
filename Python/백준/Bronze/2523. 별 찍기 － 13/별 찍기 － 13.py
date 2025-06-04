cnt = int(input())
for i in range(1,cnt+1):
    print('*' * (i))
    #print(' ' *(cnt-i),end='')
for i in range(cnt-1,0,-1):
    #print(' ' *(cnt-i),end='')
    print('*' * (i))