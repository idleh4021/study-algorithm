line =int(input()) #5
star_cnt = 1
space_cnt = line-1
stars_up = True
for i in range(1,line*2):
    print(' '*space_cnt,end='')
    print('*'*star_cnt)
    if space_cnt ==0:
        stars_up = False

    if stars_up:
        star_cnt+=2
        space_cnt-=1
    else :
        star_cnt -=2
        space_cnt +=1